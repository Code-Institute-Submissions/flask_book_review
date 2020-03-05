import os
import math
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'Books'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

def invalid_image_function():
    """ 
        Will be used globally to display images that are invalid - 
        will display a default image if an invalid image is uploaded 
    """
    books_all= mongo.db.book.find()

    # List to store books with an invalid image 
    invalid_books = []

    # Tuple - What has been declared as valid image types
    valid_img_types = ('.jpg', '.jpeg', '.png', '.gif')

    # Looks for books in the database with invalid image uploads
    for all in books_all:
        if not all['book_url'].endswith(valid_img_types) and not all['book_url'].startswith('data:image/'):
            invalid_books.append(all['book_name'])
    
    return invalid_books

    

@app.route('/')
@app.route('/home')
def home():
    
    # Query database - fiction/non-fiction books 
    non_fiction = mongo.db.book.find({
        "fact_fiction": "Non-Fiction", 
        "rating_value":  { "$in": ["5", "4"] }
        }).sort("rating_value", -1).limit(3)
    fiction = mongo.db.book.find({
        "fact_fiction": "Fiction", 
        "rating_value": { "$in": ["5", "4"] }
        }).sort("rating_value", -1).limit(3)
    
    # This will call the invalid_image_function - books with an invalid image will display a default image
    invalid_books = invalid_image_function()
    
    return render_template('index.html', 
                            non_fiction=non_fiction, 
                            fiction=fiction,
                            invalid_books=invalid_books)



@app.route('/full_book_details/<book_id>')
def full_book_details(book_id):
    
    """
    Loads the page that displays the full details of a book 
    """

    # All the books in the database 
    all_books=mongo.db.book.find()

    # Finds the individual book being displayed 
    book=mongo.db.book.find_one({'_id': ObjectId(book_id)})

    # List that will hold how many books match the genre of the book currently displayed
    book_num = []

    # Database query - find books with a matching genre 
    similar_genre_books=mongo.db.book.find({"genre_name": book["genre_name"]})
    
    # Append all the books with a matching genre to the book_num list
    for items in similar_genre_books:
        book_num.append(items)

    # List that will hold the book description
    info = []
    
    # This allows the first letter to be capitalized but still gives the user the ability to make other letters in the 
    # description capital letters 
    for k,v in book.items():
        if k == 'book_info':
            info.append(v[0].capitalize() + v[1:])
    
    # List to hold the book if it has an image uploaded that isn't valid - will be used 
    # for the main image of the book displayed
    invalid_image = []
    
    # What has been declared as valid image types
    valid_img_types = ('.jpg', '.jpeg', '.png', '.gif')

    
    # Will look for books that don't end in the specified accepted image file types from the tuple valid_img_types, and images 
    # that don't start with 'data:image/' as these are also valid images. 
    # These books will be classified as invalid images.
    if not book['book_url'].endswith(valid_img_types) and not book['book_url'].startswith('data:image/'):
        invalid_image.append(book['book_name'])
        print('image not working')
    else:
        print('image WILL work')
    
    # Will count how many books are in the invalid_image list
    count_invalid_image = len(invalid_image)

    # This will call the invalid_image_function - books with an invalid image will display a default image
    # This will be used when displaying book suggestions at the bottom of the page
    invalid_books = invalid_image_function()

    return render_template('full_book_details.html', 
                            book=book, 
                            all_books=all_books, 
                            similar_genre_books=similar_genre_books, 
                            book_num=book_num,
                            info=info,
                            count_invalid_image=count_invalid_image,
                            invalid_books=invalid_books)


""" All code for fiction related titles """

@app.route('/fiction_books')
def fiction_books():

    """ 
    Page to view all fiction books
    """
    
    # This will call the invalid_image_function - books with an invalid image will display a default image
    invalid_books = invalid_image_function()


    # Pagination
    page_limit = 6
    book_count = mongo.db.book.count({"fact_fiction": "Fiction"})
    current_page = int(request.args.get('current_page', 1))
    page = range(1, int(math.ceil(book_count / page_limit))+1)

    # Find fiction genres 
    fiction_genres=mongo.db.genre.find({'fiction': 'yes'})

    # Query the database to find fiction books, sort based on author name and apply pagination 
    fiction=mongo.db.book.find({"fact_fiction": "Fiction"}).sort("author_name", 1).skip((current_page - 1)*page_limit).limit(page_limit)

    return render_template('fiction_books.html', 
                            fiction=fiction, 
                            fiction_genres=fiction_genres,
                            page=page,
                            current_page=current_page,
                            book_count=book_count,
                            invalid_books=invalid_books)

 

@app.route('/fiction_genre_search', methods=['POST'])
def fiction_genre_search():

    """ 
    Function and results to search fiction books based on genre type 
    """

    # This will call the invalid_image_function - books with an invalid image will display a default image
    invalid_books = invalid_image_function()
    
    # Fiction genres 
    fiction_genres=mongo.db.genre.find({'fiction': 'yes'})

    # Function to find results from genre search 
    if request.method == 'POST':
        genre_name = request.form.get('genre_name')
        genre_results = mongo.db.book.find({
            'genre_name': genre_name,
            "fact_fiction": "Fiction", 
            })
        genre_count = genre_results.count()

    return render_template('fiction_genre_results.html', 
                            genre_results=genre_results,
                            fiction_genres=fiction_genres,
                            genre_count=genre_count,
                            genre_name=genre_name,
                            invalid_books=invalid_books)


@app.route('/other_fiction_books')
def other_fiction_books():

    """
    Page for books that are fiction but have been given a non-fiction genre 
    """

    # This will call the invalid_image_function - books with an invalid image will display a default image
    invalid_books = invalid_image_function()

    # Finds genres that are applied to fiction books
    fiction_genres=mongo.db.genre.find({'fiction': 'yes'})

    # List to hold books that are fiction but have a non-fiction genre 
    other_fiction_books = []
    
    # Query database - fiction books that have a non-fiction genre - will be classified as 'other' books
    other = mongo.db.book.find({
        "fact_fiction": "Fiction", 
        "genre_name": { "$in": ["Education", "Cooking", "Travel", "Biography"] }
        })
    
    # Count how many 'other' fiction books there are
    other_fiction_books_count = other.count()
    
    # Append the 'other' books found to the other_fiction_books list 
    for item in other:
        other_fiction_books.append(item)
        
    return render_template('other_fiction_books.html',
                            other_fiction_books=other_fiction_books,
                            fiction_genres=fiction_genres,
                            other_fiction_books_count=other_fiction_books_count,
                            invalid_books=invalid_books)
    


""" All code for non-fiction titles """

@app.route('/non_fiction_books')
def non_fiction_books():

    """ 
    Page for non-fiction books
    """

    # This will call the invalid_image_function - books with an invalid image will display a default image
    invalid_books = invalid_image_function()

    # Pagination
    page_limit = 6
    book_count = mongo.db.book.count({"fact_fiction": "Non-Fiction"})
    current_page = int(request.args.get('current_page', 1))
    page = range(1, int(math.ceil(book_count / page_limit)) + 1)
    
    # Shows all books in the database that are non-fiction, sorted based on author name, and with pagination
    non_fiction=mongo.db.book.find({"fact_fiction": "Non-Fiction"}).sort("author_name", 1).skip((current_page - 1)*page_limit).limit(page_limit)
    
    # Find genres that aren't fiction, i.e. that are non-fiction
    non_fiction_genres=mongo.db.genre.find({'fiction': 'no'})


    return render_template('non_fiction_books.html', 
                            non_fiction=non_fiction,
                            non_fiction_genres=non_fiction_genres,
                            current_page=current_page,
                            page=page,
                            book_count=book_count,
                            invalid_books=invalid_books)

 

@app.route('/non_fiction_genre_search', methods=['POST'])
def non_fiction_genre_search():

    """ 
    Function to filter non-fiction books based on genre type 
    """

    # This will call the invalid_image_function - books with an invalid image will display a default image
    invalid_books = invalid_image_function()

    # Finds genres that are applied to non-fiction books
    non_fiction_genres=mongo.db.genre.find({'fiction': 'no'})

    # Function to filter books by genre name 
    if request.method == 'POST':
        genre_name = request.form.get('genre_name')
        genre_results = mongo.db.book.find({
            'genre_name': genre_name,
            'fact_fiction': 'Non-Fiction'
            })
        genre_count = genre_results.count()

    return render_template('non_fiction_genre_results.html', 
                            genre_results=genre_results,
                            non_fiction_genres=non_fiction_genres,
                            genre_count=genre_count,
                            genre_name=genre_name,
                            invalid_books=invalid_books
                            )


@app.route('/other_books')
def other_books():

    """ 
    Page for non-fiction books with a genre of 'other' 
    """

    # This will call the invalid_image_function - books with an invalid image will display a default image
    invalid_books = invalid_image_function()

    # Finds genres that are applied to non-fiction books
    non_fiction_genres=mongo.db.genre.find({'fiction': 'no'})

    # Empty list to hold non-fiction books with a fiction genre i.e. 'other' books
    other_books = []
    
    # Logic that looks for books that will be classified as 'other':
    # This will be books that are non-fiction but have been given a fiction genre  
    other = mongo.db.book.find({
        "fact_fiction": "Non-Fiction", 
        "genre_name": { "$in": ["Horror", "Fantasy", "Thriller", "Crime", "Adventure"] }
        })
    
    
    # Count the number of 'other' non_fiction books
    other_books_count = other.count()
    
    # Will add books that are classified as 'other' to the other_books list
    for item in other:
        other_books.append(item)

    return render_template('other_books.html',
                            other_books=other_books,
                            non_fiction_genres=non_fiction_genres,
                            other_books_count=other_books_count,
                            invalid_books=invalid_books)



""" Functions to filter books in the database """

@app.route('/search_page/')
def search_page():

    """ 
    Landing page to filter books, and also displays all books in the database
    """

    # This will call the invalid_image_function - books with an invalid image will display a default image
    invalid_books = invalid_image_function()

    # Pagination logic 
    page_limit = 9
    book_count = mongo.db.book.count()
    current_page = int(request.args.get('current_page', 1))
    page = range(1, int(math.ceil(book_count / page_limit)) +1)

    # Displays all books, sorted based on author name, and applies pagination
    books = mongo.db.book.find().sort("author_name", 1).skip((current_page - 1)*page_limit).limit(page_limit)
    
    # Finds all genre options from the database 
    all_genre = mongo.db.genre.find()

    # Finds all rating options from the database 
    ratings = mongo.db.rating.find()


    return render_template('search_books.html', 
                            all_genre=all_genre,
                            ratings=ratings,
                            books=books,
                            page=page,
                            current_page=current_page,
                            book_count=book_count,
                            invalid_books=invalid_books)
    

 
@app.route('/search_genre')
def search_genre():

    """ 
    Landing page to filter books based on genre
    """

    # This will call the invalid_image_function - books with an invalid image will display a default image
    invalid_books = invalid_image_function()

    # Pagination logic 
    page_limit = 9
    book_count = mongo.db.book.count()
    current_page = int(request.args.get('current_page', 1))
    page = range(1, int(math.ceil(book_count / page_limit)) +1)

    # Look for all the books in the database, and sorts them based on author name. Applies pagination
    books = mongo.db.book.find().sort("author_name", 1).skip((current_page - 1)*page_limit).limit(page_limit)

    return render_template("search_genre.html", 
                            all_genre=mongo.db.genre.find(),
                            books=books,
                            current_page=current_page,
                            page=page,
                            invalid_books=invalid_books)

 
@app.route('/search_genre_function', methods=['GET', 'POST'])
def search_genre_function():

    """ 
    Function to filter books based on genre and looks for results
    """

    # This will call the invalid_image_function - books with an invalid image will display a default image
    invalid_books = invalid_image_function()

    if request.method == 'POST':
        genre_name = request.form.get('genre_name')
        results=mongo.db.book.find({"genre_name": genre_name}).sort("rating_value", -1)
        genre_count=results.count()
        
    return render_template("search_genre.html",
                            all_genre=mongo.db.genre.find(),
                            genre_name=genre_name,
                            results=results,
                            genre_count=genre_count,
                            invalid_books=invalid_books)


@app.route('/search_rating')
def search_rating():

    """ 
    Landing page to filter books based on rating
    """

    # This will call the invalid_image_function - books with an invalid image will display a default image
    invalid_books = invalid_image_function()

    # Pagination logic 
    page_limit = 9
    book_count = mongo.db.book.count()
    current_page = int(request.args.get('current_page', 1))
    page = range(1, int(math.ceil(book_count / page_limit)) +1)
    
    # Look for all the books in the database, sort by author name, applies pagination
    books = mongo.db.book.find({}).sort("author_name", 1).skip((current_page - 1)*page_limit).limit(page_limit)

    return render_template("search_rating.html",
                            all_genre=mongo.db.genre.find(),
                            ratings=mongo.db.rating.find(),
                            books=books,
                            current_page=current_page,
                            page=page,
                            invalid_books=invalid_books)


@app.route('/search_rating_function', methods=['GET', 'POST'])
def search_rating_function():

    """ 
    Function to filter books based on rating and looks for results
    """

    # This will call the invalid_image_function - books with an invalid image will display a default image
    invalid_books = invalid_image_function()

    # Look for books in the database with a rating_value that is the same 
    # as the rating_value in the form dropdown
    # Sort the results based on author name 
    if request.method == 'POST':
        rating_value = request.form.get('rating_value')
        rating_results=mongo.db.book.find({"rating_value": rating_value}).sort("author_name", 1)
        rating_count=rating_results.count()
        

    return render_template("search_rating.html",
                            ratings=mongo.db.rating.find(),
                            rating_value=rating_value,
                            rating_results=rating_results,
                            rating_count=rating_count,
                            invalid_books=invalid_books)



@app.route('/add_book')
def add_book():

    """ 
    Page user lands on to add a new book
    """

    book_genre = mongo.db.genre.find()
    rating = mongo.db.rating.find()
    fiction_non = mongo.db.type.find()

    return render_template('add_book.html', 
                            book_genre=book_genre, 
                            rating=rating, 
                            fiction_non=fiction_non)



@app.route('/insert_book', methods=['POST'])
def insert_book():

    """ 
    Function to add a new book 
    """

    books = mongo.db.book
    insert_book = books.insert_one(request.form.to_dict())
    
    return redirect(url_for("full_book_details", book_id=insert_book.inserted_id))


@app.route('/edit_book/<book_id>')
def edit_book(book_id):

    """ 
    Page user lands on to edit a book
    """

    books = mongo.db.book.find_one({"_id": ObjectId(book_id)})

    # Finds all genres from the database 
    all_genre = mongo.db.genre.find()

    # Find all rating options 
    rating = mongo.db.rating.find()

    # Find fiction/non-fiction options
    fact_fiction = mongo.db.type.find()

    # List to hold book description
    info = []
    
    # This allows the first letter to be capitalized but still gives the user the abiity to make other letters in the 
    # description capital letters 
    for k,v in books.items():
        if k == 'book_info':
            info.append(v[0].capitalize() + v[1:])

    return render_template('edit_book.html', 
                            book=books, 
                            all_genre=all_genre, 
                            rating=rating, 
                            fact_fiction=fact_fiction,
                            info=info)



@app.route('/update_book/<book_id>', methods=['POST'])
def update_book(book_id):

    """ 
    Function that is activated to edit a book
    """

    book = mongo.db.book
    book.update({"_id": ObjectId(book_id)},
    {
        'book_name':request.form.get('book_name'),
        'genre_name':request.form.get('genre_name'),
        'rating_value': request.form.get('rating_value'),
        'author_name':request.form.get('author_name'),
        'book_info':request.form.get('book_info'),
        'fact_fiction':request.form.get('fact_fiction'),
        'delete_book': request.form.get('delete_book'),
        'book_url': request.form.get('book_url'),
        'book_website': request.form.get('book_website')
    })

    return redirect(url_for("full_book_details", book_id=book_id))


@app.route('/delete_book/<book_id>')
def delete_book(book_id):

    """ 
    Function to delete a book 
    """

    mongo.db.book.remove({'_id': ObjectId(book_id)})
    return redirect(url_for('home'))

@app.errorhandler(500)
def error_500(errors):
    """
    User will be sent to this page if there is a 500 page error
    """
    return render_template("500_error.html"), 500

@app.errorhandler(404)
def error_404(errors):
    """
    User will be sent to this page if there is a 404 page error
    """
    return render_template("404_error.html"), 404

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')))
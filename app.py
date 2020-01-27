import os
import math
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'Books'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

@app.route('/')
@app.route('/home')
def home():
    
    # Query database - fiction/non-fiction books 
    non_fiction = mongo.db.book.find({
        "fact_fiction": "Non-Fiction", 
        "rating_value":  { "$in": ["5", "4"] }
        }).limit(3)
    fiction = mongo.db.book.find({
        "fact_fiction": "Fiction", 
        "rating_value": { "$in": ["5", "4"] }
        }).limit(3)
    
    return render_template('index.html', non_fiction=non_fiction, fiction=fiction)


# Loads the page that displays the full details of a book 
@app.route('/full_book_details/<book_id>')
def full_book_details(book_id):
    
    # All the books in the database 
    all_books=mongo.db.book.find()

    # Finds the individual book being displayed 
    book=mongo.db.book.find_one({'_id': ObjectId(book_id)})

    # Array that will hold how many books match the genre of the book currently displayed
    book_num = []

    # Database query - find books with a matching genre 
    similar_genre_books=mongo.db.book.find({"genre_name": book["genre_name"]})
    
    # Append all the books with a matching genre to the book_num list
    for items in similar_genre_books:
        book_num.append(items)

    
    return render_template('full_book_details.html', 
                            book=book, 
                            all_books=all_books, 
                            similar_genre_books=similar_genre_books, 
                            book_num=book_num)

# All code for fiction related titles 

# Loads page for fiction books
@app.route('/fiction_books')
def fiction_books():
    
    # Pagination
    page_limit = 6
    book_count = mongo.db.book.count({"fact_fiction": "Fiction"})
    current_page = int(request.args.get('current_page', 1))
    page = range(1, int(math.ceil(book_count / page_limit))+1)

    # Fiction genres will be displayed 
    fiction_genres=mongo.db.genre.find({'fiction': 'yes'})

    # Query the database to find fiction books, sort based on author name and apply pagination 
    fiction=mongo.db.book.find({"fact_fiction": "Fiction"}).sort("author_name", 1).skip((current_page - 1)*page_limit).limit(page_limit)
  
    return render_template('fiction_books.html', 
                            fiction=fiction, 
                            fiction_genres=fiction_genres,
                            page=page,
                            current_page=current_page,
                            book_count=book_count)

# Loads results of fiction books with the specified genre 
@app.route('/fiction_genre_results')
def fiction_genre_results():

    # Fiction genres will be displayed 
    fiction_genres=mongo.db.genre.find({'fiction': 'yes'})
    genre_name = request.form.get('genre_name')

    # 'genre_name' from form will match books with the same 'genre_name' from the database - displays results 
    genre_results = mongo.db.book.find({'genre_name': genre_name})
    
   
    return render_template('fiction_genre_results.html',
                            fiction_genres=fiction_genres,
                            genre_results=genre_results
    )

# Function to search fiction books based on genre type 
@app.route('/fiction_genre_search', methods=['POST'])
def fiction_genre_search():
    
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
                            genre_name=genre_name)

# Books that are fiction but have a non-fiction genre 
@app.route('/other_fiction_books')
def other_fiction_books():

    # Finds genres that are applied to fiction books
    fiction_genres=mongo.db.genre.find({'fiction': 'yes'})

    # List to hold books that are fiction but have a non-fiction genre 
    other_fiction_books = []
    
    other = mongo.db.book.find({
        
        "fact_fiction": "Fiction", 
        "genre_name": { "$in": ["Education", "Cooking", "Travel", "Biography"] }
        })
    
    other_fiction_books_count = other.count()
    
    for item in other:
        other_fiction_books.append(item)
        
    return render_template('other_fiction_books.html',
                            other_fiction_books=other_fiction_books,
                            fiction_genres=fiction_genres,
                            other_fiction_books_count=other_fiction_books_count)
    


# All code for non-fiction titles 

# Loads non-fiction books
@app.route('/non_fiction_books')
def non_fiction_books():

    # Empty list to hold non-fiction books with a fiction genre 
    other_books = []

    # Pagination
    page_limit = 6
    book_count = mongo.db.book.count({"fact_fiction": "Non-Fiction"})
    current_page = int(request.args.get('current_page', 1))
    page = range(1, int(math.ceil(book_count / page_limit)) + 1)
    

    # Shows all books in the database that are non-fiction, sorted based on author name, and with pagination
    non_fiction=mongo.db.book.find({"fact_fiction": "Non-Fiction"}).sort("author_name", 1).skip((current_page - 1)*page_limit).limit(page_limit)
    
    # Logic that looks for books that will be classified as 'other':
    # This will be books that are non-fiction but have been given a fiction genre 
    other = mongo.db.book.find({
        
        "fact_fiction": "Non-Fiction", 
        "genre_name": { "$in": ["Horror", "Fantasy", "Thriller", "Crime", "Adventure"] }
        })


    # Looks for books that aren't fiction genres i.e. non-fiction
    non_fiction_genres=mongo.db.genre.find({'fiction': 'no'})

    # Will add books that are classified as 'other' genre to the other_books list
    for item in other:
        other_books.append(item)
    
    return render_template('non_fiction_books.html', 
                            non_fiction=non_fiction,
                            non_fiction_genres=non_fiction_genres,
                            current_page=current_page,
                            page=page,
                            other=other,
                            other_books=other_books,
                            book_count=book_count)

# Loads results of non-fiction books with the specified genre 
@app.route('/non_fiction_genre_results')
def non_fiction_genre_results():

    # Finds non-fiction genres
    non_fiction_genres=mongo.db.genre.find({'fiction': 'no'})
    genre_name = request.form.get('genre_name')

    # Find books that match genre_name from the form to the genre_name from the database 
    genre_results = mongo.db.book.find({'genre_name': genre_name})
    
   
    return render_template('non_fiction_genre_results.html',
                            non_fiction_genres=non_fiction_genres,
                            genre_results=genre_results
    )

# Function to search non-fiction books based on genre type 
@app.route('/non_fiction_genre_search', methods=['POST'])
def non_fiction_genre_search():
    
    # Finds genres that are applied to non-fiction books
    non_fiction_genres=mongo.db.genre.find({'fiction': 'no'})

    # List that will hold the books that have 'other' genre 
    other_books = []
    
    # Will look for non-fiction books that have been given a fiction genre 
    other = mongo.db.book.find({
        
        "fact_fiction": "Non-Fiction", 
        "genre_name": { "$in": ["Horror", "Fantasy", "Thriller", "Crime", "Adventure"] }
        })

    # Adds the non-fiction books with a fiction genre to the other_books list
    for item in other:
        other_books.append(item)
    

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
                            other_books=other_books,
                            genre_name=genre_name
                            )

# Loads 'other' genre non-fiction books
@app.route('/other_books')
def other_books():

    # Finds genres that are applied to non-fiction books
    non_fiction_genres=mongo.db.genre.find({'fiction': 'no'})

    # List to hold books that have a fiction genre 
    other_books = []
    
    other = mongo.db.book.find({
        
        "fact_fiction": "Non-Fiction", 
        "genre_name": { "$in": ["Horror", "Fantasy", "Thriller", "Crime", "Adventure"] }
        })
    
    other_books_count = other.count()
    
    for item in other:
        other_books.append(item)

    return render_template('other_books.html',
                            other_books=other_books,
                            non_fiction_genres=non_fiction_genres,
                            other_books_count=other_books_count)


# Functions to search all books in the database 

# Landing page to search books and also displays all books in the database
@app.route('/search_page/')
def search_page():

    # Pagination
    page_limit = 6 
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
                            book_count=book_count)
    

# Landing page to search genre 
@app.route('/search_genre')
def search_genre():

    # Look for all books from the database, sort based on author name 
    books = mongo.db.book.find().sort("author_name", 1)
    genre_name = request.form.get('genre_name')
    genre_result=mongo.db.book.find({"genre_name": genre_name})

    return render_template("search_genre.html", 
                            all_genre=mongo.db.genre.find(),
                            ratings=mongo.db.rating.find(),
                            genre_result=genre_result,
                            books=books)

# Function to search based on genre 
@app.route('/search_genre_function', methods=['GET', 'POST'])
def search_genre_function():

    if request.method == 'POST':
        genre_name = request.form.get('genre_name')
        results=mongo.db.book.find({"genre_name": genre_name}).sort("rating_value", -1)
        genre_count=results.count()
        
    return render_template("search_genre.html",
                            all_genre=mongo.db.genre.find(),
                            genre_name=genre_name,
                            results=results,
                            genre_count=genre_count)


# Landing page to search rating
@app.route('/search_rating')
def search_rating():
    return render_template("search_rating.html",
                            all_genre=mongo.db.genre.find(),
                            ratings=mongo.db.rating.find())

# Function to search based on rating 
@app.route('/search_rating_function', methods=['GET', 'POST'])
def search_rating_function():

    if request.method == 'POST':
        rating_value = request.form.get('rating_value')
        rating_results=mongo.db.book.find({"rating_value": rating_value}).sort("author_name", 1)
        rating_count=rating_results.count()
        

    return render_template("search_rating.html",
                            ratings=mongo.db.rating.find(),
                            rating_value=rating_value,
                            rating_results=rating_results,
                            rating_count=rating_count)


# Page user lands on to add a new book
@app.route('/add_book')
def add_book():
    book_genre = mongo.db.genre.find()
    rating = mongo.db.rating.find()
    fiction_non = mongo.db.type.find()
    return render_template('add_book.html', book_genre=book_genre, rating=rating, fiction_non=fiction_non)


# Function to add a new book 
@app.route('/insert_book', methods=['POST'])
def insert_book():
    books = mongo.db.book
    books.insert_one(request.form.to_dict())
    
    return redirect(url_for('home'))

# Page user lands on to edit book
@app.route('/edit_book/<book_id>')
def edit_book(book_id):
    books = mongo.db.book.find_one({"_id": ObjectId(book_id)})

    # Finds all genres from the database 
    all_genre = mongo.db.genre.find()

    # Find all rating options 
    rating = mongo.db.rating.find()

    # Find fiction/non-fiction options
    fact_fiction = mongo.db.type.find()

    return render_template('edit_book.html', book=books, all_genre=all_genre, rating=rating, fact_fiction=fact_fiction)


# Function that is activated to edit a book
@app.route('/update_book/<book_id>', methods=['POST'])
def update_book(book_id):
    
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

    return redirect(url_for( "full_book_details", book_id=book_id))

# Function to delete a book 
@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    
    mongo.db.book.remove({'_id': ObjectId(book_id)})
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
import os
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
    all_books = mongo.db.book.find()

    # Query database - fiction/non-fiction books 
    non_fiction = mongo.db.book.find({"fact_fiction": "Non-Fiction", "rating_value": "3"})
    fiction = mongo.db.book.find({"fact_fiction": "Fiction", "rating_value": "4" })
    
    return render_template('index.html', all_books=all_books, non_fiction=non_fiction, fiction=fiction)

@app.route('/full_book_details/<book_id>')
def full_book_details(book_id):
    book=mongo.db.book.find_one({'_id': ObjectId(book_id)})
    
    return render_template('full_book_details.html', book=book)

@app.route('/fiction_books')
def fiction_books():
    
    fiction=mongo.db.book.find({"fact_fiction": "Fiction"})
    return render_template('fiction_books.html', fiction=fiction)

@app.route('/non_fiction_books')
def non_fiction_books():
    
    non_fiction=mongo.db.book.find({"fact_fiction": "Non-Fiction"})
    return render_template('non_fiction_books.html', non_fiction=non_fiction)


@app.route('/search_page/')
def search_page():
    
    return render_template(
        'search_books.html', 
        all_genre=mongo.db.genre.find(),
        ratings=mongo.db.rating.find())

@app.route('/search_book_function/', methods=['GET', 'POST'])
def search_book_function():
    
    if request.method == 'POST':
        # genre 
        all_genre=mongo.db.genre.find()


        # ratings 
        ratings=mongo.db.rating.find()

        if all_genre:
            genre_name = request.form.get('genre_name')
            results=mongo.db.book.find({"genre_name": genre_name})
        
        if ratings:
            rating_value = request.form.get('rating_value')
            rating_results=mongo.db.book.find({"rating_value": rating_value})
        
        
        return render_template('search_books.html', 
                                all_genre=mongo.db.genre.find(), 
                                ratings=mongo.db.rating.find(),
                                results=results,
                                rating_results=rating_results,
                                rating_count=rating_results.count(),
                                genre_count=results.count())
    
        
    else:
        return render_template('search_books.html', all_genre=mongo.db.genre.find())    

@app.route('/add_book')
def add_book():
    book_genre = mongo.db.genre.find()
    rating = mongo.db.rating.find()
    fiction_non = mongo.db.type.find()
    return render_template('add_book.html', book_genre=book_genre, rating=rating, fiction_non=fiction_non)

@app.route('/insert_book', methods=['POST'])
def insert_book():

    books = mongo.db.book
    books.insert_one(request.form.to_dict())

    return redirect(url_for('home'))

@app.route('/edit_book/<book_id>')
def edit_book(book_id):
    books = mongo.db.book.find_one({"_id": ObjectId(book_id)})
    all_genre = mongo.db.genre.find()
    rating = mongo.db.rating.find()
    fact_fiction = mongo.db.type.find()

    return render_template('edit_book.html', book=books, all_genre=all_genre, rating=rating, fact_fiction=fact_fiction)

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
        'book_url': request.form.get('book_url')
    })

    return redirect(url_for('home'))

@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    
    mongo.db.book.remove({'_id': ObjectId(book_id)})
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
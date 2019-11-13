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
    
    return render_template('index.html', all_books=all_books)

@app.route('/full_book_details/<book_id>')
def full_book_details(book_id):
    book=mongo.db.book.find_one({'_id': ObjectId(book_id)})

    return render_template('full_book_details.html', book=book)

@app.route('/search_page/')
def search_page():
    
    return render_template(
        'search_books.html', 
        all_genre=mongo.db.genre.find())

@app.route('/search_book_function/', methods=['GET', 'POST'])
def search_book_function():
    
    if request.method == 'POST':
        # Query database, render search template w/ results
        
        genre_name = request.form.get('genre_name')
        results=mongo.db.book.find({"genre_name": genre_name})
        
        
        return render_template('search_books.html', 
                                all_genre=mongo.db.genre.find(), 
                                results=results,
                                genre_count=results.count())
    
        
    else:
        return render_template('search_books.html', all_genre=mongo.db.genre.find())    

@app.route('/add_book')
def add_book():
    book_genre = mongo.db.genre.find()
    rating = mongo.db.rating.find()
    return render_template('add_book.html', book_genre=book_genre, rating=rating)

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

    return render_template('edit_book.html', book=books, all_genre=all_genre, rating=rating)

@app.route('/update_book/<book_id>', methods=['POST'])
def update_book(book_id):
    book = mongo.db.book
    book.update({"_id": ObjectId(book_id)},
    {
        'book_name':request.form.get('book_name'),
        'genre_name':request.form.get('genre_name'),
        'rating_value': request.form.get('rating_value'),
        'author_name':request.form.get('author_name'),
        'book_info':request.form.get('book_info')
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
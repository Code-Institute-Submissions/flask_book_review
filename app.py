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

@app.route('/search_books')
def search_books():
    return render_template('search_books.html')

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

@app.route('/edit_book/<book_id>', methods=['GET, POST'])
def edit_book(book_id):
    books = mongo.db.book
    return redirect(url_for('full_book_details'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from models import db, Author, Book, Review

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book_reviews.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = True

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return make_response(jsonify({"message": "Welcome to the Book Reviews API"}), 200)

@app.route('/books', methods=['GET'])
def get_all_books():
    books = Book.query.all()
    return make_response(jsonify([book.serialize() for book in books]), 200)

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(title=data['title'], author_id=data['author_id'])
    db.session.add(new_book)
    db.session.commit()
    return make_response(jsonify(new_book.serialize()), 201)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return make_response(jsonify(book.serialize()), 200)

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = Book.query.get_or_404(book_id)
    book.title = data.get('title', book.title)
    db.session.commit()
    return make_response(jsonify(book.serialize()), 200)

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return make_response(jsonify({"message": "Book deleted"}), 204)
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Author, Book, Review

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return "Welcome to the Book Review Platform API!"


@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get(id)
    if not book:
        abort(404, description="Book not found.")
    return jsonify(book.to_dict())

@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    title = data.get('title')
    publication_year = data.get('publication_year')
    author_id = data.get('author_id')

    if not all([title, publication_year, author_id]):
        abort(400, description="Missing fields.")

    author = Author.query.get(author_id)
    if not author:
        abort(404, description="Author not found.")

    new_book = Book(title=title, publication_year=publication_year, author=author)
    db.session.add(new_book)
    db.session.commit()

    return jsonify(new_book.to_dict()), 201

@app.route('/books/<int:id>', methods=['PATCH'])
def update_book(id):
    book = Book.query.get(id)
    if not book:
        abort(404, description="Book not found.")

    data = request.get_json()
    book.title = data.get('title', book.title)
    book.publication_year = data.get('publication_year', book.publication_year)

    db.session.commit()
    return jsonify(book.to_dict())

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if not book:
        abort(404, description="Book not found.")

   
    for review in book.reviews:
        db.session.delete(review)

    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)

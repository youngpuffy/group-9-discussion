from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()
db = SQLAlchemy(metadata= metadata)

class Author(db.Model, SerializerMixin):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)

    books = db.relationship('Book', backref='author', lazy= True)

class Book(db.Model, SerializerMixin):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    publication_year =db.Column(db.Integer, nullable=False)

    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    reviews = db.relationship('Review', secondary=book_review, backref=db.backref('books', lazy='dynamic'),lazy='dynamic')
    



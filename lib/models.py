from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()
db = SQLAlchemy(metadata= metadata)

book_review =db.Table(
    'book_review',
    db.Column('book_id', db.Integer, db.Foreignkey('books.id'), primary_key=True),  
     db.Column('review_id', db.Integer, db.Foreignkey('reviews.id'), primary_key=True)               
 )
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

class  Review(db.Model):
    __tablename__ ='reviews'

    id =db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)




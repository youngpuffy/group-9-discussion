from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    books = db.relationship('Book', backref='author', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'books': [book.serialize() for book in self.books]
        }

class Book(db.Model):
    __tablename__ = 'books'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    reviews = db.relationship('Review', secondary='book_reviews', backref='books', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'author_id': self.author_id,
            'reviews': [review.serialize() for review in self.reviews]
        }

class Review(db.Model):
    __tablename__ = 'reviews'
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'content': self.content,
            'rating': self.rating
        }

book_reviews = db.Table('book_reviews',
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True),
    db.Column('review_id', db.Integer, db.ForeignKey('reviews.id'), primary_key=True)
)
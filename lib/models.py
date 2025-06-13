from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    books = db.relationship('Book', backref='author', cascade="all, delete-orphan")

    def to_dict(self):
        return {"id": self.id, "name": self.name}


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    publication_year = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

    reviews = db.relationship('Review', backref='book', cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "publication_year": self.publication_year,
            "author": self.author.name if self.author else None,
            "reviews": [review.to_dict() for review in self.reviews]
        }


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "comment": self.comment
        }
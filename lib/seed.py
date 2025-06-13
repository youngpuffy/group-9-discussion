from models import db, Author, Book, Review
from app import app

def seed_database():
    with app.app_context():
        db.drop_all()
        db.create_all()

    author1 = Author(name="George Orwell")
    author2 = Author(name="J.K. Rowling")

    book1 = Book(title="1984", publication_year=1949, author=author1)
    book2 = Book(title="Animal Farm", publication_year=1945, author=author1)
    book3 = Book(title="Harry Potter and the Philosopher's Stone", publication_year=1997, author=author2)
    book4 = Book(title="Harry Potter and the Chamber of Secrets", publication_year=1998, author=author2)

    review1 = Review(rating=5, comment="Amazing!", book=book1)
    review2 = Review(rating=4, comment="Thought-provoking", book=book1)
    review3 = Review(rating=5, comment="Brilliant satire", book=book2)
    review4 = Review(rating=3, comment="Good read", book=book3)
    review5 = Review(rating=4, comment="Magical!", book=book3)
    review6 = Review(rating=5, comment="Loved it", book=book4)

    db.session.add_all([author1, author2, book1, book2, book3, book4,
                        review1, review2, review3, review4, review5, review6])
    db.session.commit()

    print("Database seeded successfully.")
if name == "main":
    seed_database()

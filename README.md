Group 9 Book Review Discussion App
A Flask-based web application for managing authors, books, and book reviews. It leverages SQLAlchemy for object-relational mapping (ORM) and supports serialization for seamless API responses.
Features

Create, read, update, and delete authors and their books
Relational database management with SQLAlchemy

Project Structure
group-9-discussion/
│
├── Pipfile                # Dependency management
├── Pipfile.lock           # Locked dependency versions
├── README.md              # Project documentation
└── lib/
    ├── app.py             # Main Flask application
    ├── models.py          # SQLAlchemy model definitions
    └── seed.py            # Database seeding script

Installation
Prerequisites

Python 3.8 or higher
pipenv (install with pip install pipenv)

Steps

Clone the Repository:
git clone https://github.com/youngpuffy/group-9-discussion.git
cd group-9-discussion


Install Dependencies:
pipenv install


Activate the Virtual Environment:
pipenv shell


Run the Application:
python lib/app.py



Models Overview

Author: Represents a book author with attributes like name and relationships to books.
Book: Represents a book, linked to an author via a foreign key.
Review: Represents a review, associated with a specific book.

See lib/models.py for detailed model definitions.
Usage

The application runs on http://localhost:5000 by default.
Use API endpoints to manage authors, books, and reviews (refer to lib/app.py for available routes).
Seed the database with sample data using:python lib/seed.py



Contributing

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit (git commit -m "Add feature").
Push to the branch (git push origin feature-branch).
Open a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

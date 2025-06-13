# Flask SQLAlchemy Book Reviews API

## Overview
This project is a Flask application that provides a RESTful API for managing book reviews. It allows users to retrieve, add, update, and delete books, authors, and reviews. The application uses Flask-SQLAlchemy for database interactions and Flask-Migrate for handling database migrations.

## Project Structure
```
flask_sqlalchemy_app
├── app.py            # Main entry point of the Flask application
├── models.py         # SQLAlchemy models for Author, Book, and Review
├── seed.py           # Script to populate the database with initial data
├── requirements.txt   # List of dependencies for the project
├── migrations         # Directory containing migration scripts
│   └── README         # Information about managing database migrations
├── sql_alchemy.py     # Database setup and configuration for SQLAlchemy
└── README.md          # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd flask_sqlalchemy_app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Initialize the database:**
   ```
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

5. **Seed the database with initial data:**
   ```
   python seed.py
   ```

## Usage
To run the application, use the following command:
```
flask run
```
The API will be available at `http://127.0.0.1:5000/`.

## API Endpoints
- `GET /` - Welcome message
- `GET /books` - Retrieve all books
- `GET /books/<int:book_id>` - Retrieve a specific book by ID

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.
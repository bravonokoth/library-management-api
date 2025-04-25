# Library Management API

## Description
This project is a CRUD API for a Library Management System, built using **FastAPI** (Python) and connected to a **MySQL** database. It allows users to manage books and their categories, supporting Create, Read, Update, and Delete (CRUD) operations. The API is designed to handle book inventory and category management for a library.

### Features
- Manage book categories (e.g., Fiction, Non-Fiction).
- Manage books with details like title, ISBN, publication year, and availability.
- RESTful endpoints for CRUD operations on `Categories` and `Books`.
- MySQL database with proper relationships (1-M between Categories and Books).

## Setup and Installation

### Prerequisites
- Python 3.8+
- MySQL Server
- Git
- A code editor (e.g., VS Code)

### Steps
1. **Clone the Repository**:
  
   git clone https://github.com/your-username/library-management-api.git

   cd library-management-api

## Install Dependencies:


pip install -r requirements.txt

## Set Up the MySQL Database:
Create a MySQL database named library_management.

Update the DATABASE_URL in src/database.py with your MySQL credentials (e.g., root:your_password@localhost/library_management).

Run the SQL script to set up the database:


mysql -u root -p library_management < sql/library_management.sql

Run the API:


uvicorn src.main:app --reload

The API will be available at http://localhost:8000.

Access the interactive API documentation at http://localhost:8000/docs.

## Database Schema

The database includes the following tables:
Categories: Stores book categories (e.g., Fiction, Non-Fiction).

Books: Stores book details with a foreign key to Categories.

Other Tables (not used in API): Members, Authors, BookAuthors, Loans (for full system context).

See sql/library_management.sql for the complete schema.

## ERD
The Entity-Relationship Diagram (ERD) is available as erd.png in the project root. It illustrates the 1-M relationship between Categories and Books.
ERD

## API Endpoints
Categories:
POST /categories/ - Create a new category

GET /categories/{category_id} - Read a category by ID

GET /categories/ - List all categories

PUT /categories/{category_id} - Update a category

DELETE /categories/{category_id} - Delete a category

Books:
POST /books/ - Create a new book

GET /books/{book_id} - Read a book by ID

GET /books/ - List all books

PUT /books/{book_id} - Update a book

DELETE /books/{book_id} - Delete a book

## Project Structure

library-management-api/
├── src/
│   ├── main.py             # FastAPI application
│   ├── database.py         # Database connection
│   ├── models.py           # Pydantic models
│   ├── schemas.py          # SQLAlchemy models
│   ├── crud.py             # CRUD operations
├── sql/
│   ├── library_management.sql  # Database schema
├── erd.png                 # ERD screenshot
├── requirements.txt        # Dependencies
├── README.md               # Documentation

## How to Test 

Use the interactive API docs at http://localhost:8000/docs to test endpoints.

Example request to create a category:
json

POST /categories/
{
    "CategoryName": "Mystery",
    "Description": "Mystery and thriller books"
}

Example request to create a book:
json

POST /books/
{
    "Title": "The Da Vinci Code",
    "ISBN": "9780307474278",
    "PublicationYear": 2003,
    "CategoryID": 1,
    "TotalCopies": 5,
    "AvailableCopies": 5
}

## Notes

Ensure the MySQL server is running before starting the API.

The library_management.sql file includes sample data for testing.

The ERD was generated using MySQL Workbench (or dbdiagram.io).

## About
This project was developed as part of the Power Learn Project - Software Development Cohort VII (February 2025).


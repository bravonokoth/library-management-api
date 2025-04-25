cat << 'EOF' > src/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import Category, CategoryCreate, Book, BookCreate
from crud import (
    create_category, get_category, get_categories, update_category, delete_category,
    create_book, get_book, get_books, update_book, delete_book
)

app = FastAPI(title="Library Management API")

# Category Endpoints
@app.post("/categories/", response_model=Category)
def create_new_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, category)

@app.get("/categories/{category_id}", response_model=Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = get_category(db, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@app.get("/categories/", response_model=List[Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_categories(db, skip, limit)

@app.put("/categories/{category_id}", response_model=Category)
def update_existing_category(category_id: int, category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = update_category(db, category_id, category)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@app.delete("/categories/{category_id}")
def delete_existing_category(category_id: int, db: Session = Depends(get_db)):
    db_category = delete_category(db, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"detail": "Category deleted"}

# Book Endpoints
@app.post("/books/", response_model=Book)
def create_new_book(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book)

@app.get("/books/{book_id}", response_model=Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = get_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.get("/books/", response_model=List[Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_books(db, skip, limit)

@app.put("/books/{book_id}", response_model=Book)
def update_existing_book(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
    db_book = update_book(db, book_id, book)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.delete("/books/{book_id}")
def delete_existing_book(book_id: int, db: Session = Depends(get_db)):
    db_book = delete_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"detail": "Book deleted"}
EOF
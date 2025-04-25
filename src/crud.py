cat << 'EOF' > src/crud.py
from sqlalchemy.orm import Session
from schemas import Category, Book
from models import CategoryCreate, BookCreate

# Category CRUD
def create_category(db: Session, category: CategoryCreate):
    db_category = Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.CategoryID == category_id).first()

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Category).offset(skip).limit(limit).all()

def update_category(db: Session, category_id: int, category: CategoryCreate):
    db_category = db.query(Category).filter(Category.CategoryID == category_id).first()
    if db_category:
        for key, value in category.dict().items():
            setattr(db_category, key, value)
        db.commit()
        db.refresh(db_category)
    return db_category

def delete_category(db: Session, category_id: int):
    db_category = db.query(Category).filter(Category.CategoryID == category_id).first()
    if db_category:
        db.delete(db_category)
        db.commit()
    return db_category

# Book CRUD
def create_book(db: Session, book: BookCreate):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.BookID == book_id).first()

def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Book).offset(skip).limit(limit).all()

def update_book(db: Session, book_id: int, book: BookCreate):
    db_book = db.query(Book).filter(Book.BookID == book_id).first()
    if db_book:
        for key, value in book.dict().items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = db.query(Book).filter(Book.BookID == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book
EOF
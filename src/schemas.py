from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Category(Base):
    __tablename__ = "Categories"
    CategoryID = Column(Integer, primary_key=True, index=True)
    CategoryName = Column(String(50), unique=True, nullable=False)
    Description = Column(String(255))

class Book(Base):
    __tablename__ = "Books"
    BookID = Column(Integer, primary_key=True, index=True)
    Title = Column(String(255), nullable=False)
    ISBN = Column(String(13), unique=True, nullable=False)
    PublicationYear = Column(Integer)
    CategoryID = Column(Integer, ForeignKey("Categories.CategoryID"), nullable=False)
    TotalCopies = Column(Integer, nullable=False)
    AvailableCopies = Column(Integer, nullable=False)
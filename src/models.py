cat << 'EOF' > src/models.py
from pydantic import BaseModel, Field

class CategoryBase(BaseModel):
    CategoryName: str = Field(..., max_length=50)
    Description: str | None = None

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    CategoryID: int

    class Config:
        from_attributes = True

class BookBase(BaseModel):
    Title: str = Field(..., max_length=255)
    ISBN: str = Field(..., max_length=13)
    PublicationYear: int | None = None
    CategoryID: int
    TotalCopies: int = Field(..., ge=0)
    AvailableCopies: int = Field(..., ge=0)

class BookCreate(BookBase):
    pass

class Book(BookBase):
    BookID: int

    class Config:
        from_attributes = True
EOF
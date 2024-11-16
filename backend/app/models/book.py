""" Book models """
from sqlmodel import Field, SQLModel
from typing import Optional
from .base import SQLModel

# Shared properties
class BookBase(SQLModel):
    title: str = Field(index=True)
    authors: str
    synopsis: str | None = None
    buy_link: str | None = None
    genres: str
    rating: float
    editorial: str | None = None
    comments: str | None = None
    publication_date: str
    image: str | None = None

# Database model, table inferred from class name
class Book(BookBase, table=True):
    id_book: int | None = Field(default=None, primary_key=True)

# Properties to receive via API on creation
class BookCreate(BookBase):
    pass

# Properties to receive via API on update, all are optional
class BookUpdate(SQLModel):
    title: Optional[str] = None
    authors: Optional[str] = None
    synopsis: Optional[str] = None
    buy_link: Optional[str] = None
    genres: Optional[str] = None
    rating: Optional[float] = None
    editorial: Optional[str] = None
    comments: Optional[str] = None
    publication_date: Optional[str] = None
    image: Optional[str] = None

# Properties to return via API
class BookOut(BookBase):
    id_book: int

class BooksOut(SQLModel):
    data: list[BookOut]
    count: int


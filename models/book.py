from pydantic import BaseModel
from fastapi import Query
from .author import Author


class Book(BaseModel):
    isbn: str
    name: str
    author: Author
    year: int


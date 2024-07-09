from datetime import date
from typing import Optional
from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    published_date: date
    isbn: str
    pages: int
    id: Optional[int] = None

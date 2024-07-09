import sqlite3
from datetime import datetime
from typing import Optional, List

from src.api.models.book import Book
from src.api.utils.const import SQLITE_DATABASE
from src.api.utils.error_handlers import NotFoundException


class BaseDAO:
    def __init__(self, db_file: str):
        self.db_file = db_file

    def _connect(self):
        return sqlite3.connect(self.db_file)


class BookDAO(BaseDAO):
    def __init__(self, *args, **kwargs: str):
        super().__init__(*args, **kwargs)

    def create_table(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title VARCHAR(255) NOT NULL,
                    author VARCHAR(100) NOT NULL,
                    published_date DATE NOT NULL,
                    isbn VARCHAR(20) UNIQUE NOT NULL,
                    pages INTEGER NOT NULL
                );
            ''')
            conn.commit()

    def create_book(self, book: Book):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO books (title, author, published_date, isbn, pages)
                VALUES (?, ?, ?, ?, ?)
            ''', (book.title, book.author, book.published_date, book.isbn, book.pages))
            conn.commit()
            book.id = cursor.lastrowid
        return book

    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT title, author, published_date, isbn, pages, id FROM books WHERE id = ?', (book_id,))
            row = cursor.fetchone()
            if row:
                row = list(row)
                row[2] = datetime.strptime(row[2], '%Y-%m-%d').date()
                return Book(*row)
            raise NotFoundException("Book not found")

    def get_all_books(self) -> List[Book]:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT title, author, published_date, isbn, pages, id FROM books')
            rows = cursor.fetchall()

            books = []
            for row in rows:
                row = list(row)
                row[2] = datetime.strptime(row[2], '%Y-%m-%d').date()
                books.append(Book(*row))

            return books

    def update_book(self, book: Book) -> Book:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE books
                SET title = ?, author = ?, published_date = ?, isbn = ?, pages = ?
                WHERE id = ?
            ''', (book.title, book.author, book.published_date, book.isbn, book.pages, book.id))
            conn.commit()
        if cursor.rowcount == 0:
            raise NotFoundException("Book not found")
        return book

    def delete_book(self, book_id: int):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
            conn.commit()
        if cursor.rowcount == 0:
            raise NotFoundException("Book not found")


book_dao = BookDAO(SQLITE_DATABASE)

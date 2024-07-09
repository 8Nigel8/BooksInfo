from src.api.daos.daos import book_dao
from src.api.schemas.book_schema import books_schema, book_schema


class BookService:

    def get_books(self):
        books = book_dao.get_all_books()
        return books_schema.dump(books)

    def create_book(self, data):
        book = book_schema.load(data, many=False)
        created_book = book_dao.create_book(book)
        return book_schema.dump(created_book)

    def update_book(self, data, book_id):
        book = book_schema.load(data)
        book.id = book_id
        updated_book = book_dao.update_book(book)
        return book_schema.dump(updated_book)

    def delete_book(self, book_id):
        book_dao.delete_book(book_id)

    def get_book_by_id(self, book_id):
        book = book_dao.get_book_by_id(book_id)
        return book_schema.dump(book)


book_service = BookService()

import re
from datetime import date

from marshmallow import Schema, fields, validates, ValidationError, post_load

from src.api.models.book import Book


class BookSchema(Schema):
    class Meta:
        model = Book
        load_instance = True

    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    author = fields.Str(required=True)
    published_date = fields.Date(required=True)
    isbn = fields.Str(required=True)
    pages = fields.Int(required=True)

    @validates('title')
    def validate_title(self, value):
        if len(value) < 1:
            raise ValidationError('Title cannot be empty')

    @validates('author')
    def validate_author(self, value):
        if len(value) < 1:
            raise ValidationError('Author cannot be empty')

    @validates('published_date')
    def validate_published_date(self, value):
        if value > date.today():
            raise ValidationError('Published date cannot be in the future')

    @validates('isbn')
    def validate_isbn(self, value):
        if not (self.is_valid_isbn(value)):
            raise ValidationError('Invalid ISBN')

    @validates('pages')
    def validate_pages(self, value):
        if value < 1:
            raise ValidationError('Pages count cannot be less than 1')

    @post_load
    def make_book(self, data, **kwargs):
        return Book(**data)

    def is_valid_isbn(self, isbn):
        if len(isbn) != 10:
            return False
        if not re.match(r'^\d{9}[\dX]$', isbn):
            return False
        total = sum((i + 1) * (10 if x == 'X' else int(x)) for i, x in enumerate(isbn))
        return total % 11 == 0


book_schema = BookSchema()
books_schema = BookSchema(many=True)

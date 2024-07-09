from flask import Blueprint, request

from src.api.services.book_service import book_service
from src.api.utils.common import generate_response

book_bp = Blueprint('book', __name__, url_prefix='/books')


@book_bp.route('', methods=['GET'])
def get_books():
    books = book_service.get_books()
    return generate_response(200, books)


@book_bp.route('', methods=['POST'])
def create_book():
    data = request.get_json()
    book = book_service.create_book(data)
    return generate_response(201, book)


@book_bp.route('/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = book_service.update_book(data, book_id)
    return generate_response(200, book)


@book_bp.route('/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book_service.delete_book(book_id)
    return generate_response(200)


@book_bp.route('/<int:book_id>', methods=['GET'])
def get_book_by_id(book_id):
    book = book_service.get_book_by_id(book_id)
    return generate_response(200, book)

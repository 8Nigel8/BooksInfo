import traceback
from sqlite3 import IntegrityError

from marshmallow import ValidationError


class NotFoundException(Exception):
    pass


def add_error_handlers(app):

    @app.errorhandler(Exception)
    def handle_exception(e: Exception):
        return {
            'status': 'failure',
            'error': 'InternalServerError',
            'message': str(e)
        }, 500

    @app.errorhandler(NotFoundException)
    def handle_not_found(e: NotFoundException):
        return {
            'status': 'Not found',
            'error': 'Not Found',
            'message': str(e)
        }, 404

    @app.errorhandler(ValidationError)
    def handle_validation_error(e: ValidationError):
        return {
            'status': 'failure',
            'error': 'ValidationError',
            'message': str(e)
        }, 400

    @app.errorhandler(IntegrityError)
    def handle_integrity_error(e: IntegrityError):
        return {
            'status': 'failure',
            'error': 'IntegrityError',
            'message': str(e)
        }, 400

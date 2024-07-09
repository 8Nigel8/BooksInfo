from flask import Flask
from flask_cors import CORS

from src.api.daos.daos import book_dao
from src.api.endpoints.book import book_bp
from src.api.utils.config import config
from src.api.utils.error_handlers import add_error_handlers


class __PrefixMiddleware(object):

    def __init__(self, app, prefix=''):
        self.app = app
        self.prefix = prefix

    def __call__(self, environ, start_response):
        if environ['PATH_INFO'].startswith(self.prefix):
            environ['PATH_INFO'] = environ['PATH_INFO'][len(self.prefix):]
            environ['SCRIPT_NAME'] = self.prefix
            return self.app(environ, start_response)
        else:
            start_response('404', [('Content-Type', 'text/plain')])
            return ["This url does not belong to the app.".encode()]


def init_db():
    book_dao.create_table()


def create_app():
    app = Flask(__name__)

    app.wsgi_app = __PrefixMiddleware(app.wsgi_app, prefix=f'/api')

    app.config.from_object(config)

    cors = CORS()
    cors.init_app(app)
    app.register_blueprint(book_bp)

    add_error_handlers(app)
    return app

from src.api.utils.const import FLASK_SECRET_KEY


class Config:
    SECRET_KEY = FLASK_SECRET_KEY


config = Config()

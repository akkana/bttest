
import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'NOT-REALLY-SECRET'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') \
        or "sqlite:///test.db"


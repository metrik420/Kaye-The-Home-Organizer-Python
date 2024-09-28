import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///organizer.db'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_TYPE = "simple"
    CACHE_DEFAULT_TIMEOUT = 300


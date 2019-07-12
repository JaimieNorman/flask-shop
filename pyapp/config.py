import os


class Config:
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # Below uses environment variables to keep information safe
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
    SECRET_KEY = '12389ydsahjdb129371hjksd'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'

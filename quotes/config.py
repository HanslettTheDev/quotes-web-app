# from boto.s3.connection import S3Connection
import os

# s3 = S3Connection(os.environ['SECRET_KEY'], os.environ['DATABASE_URI'], os.environ['mail_username'], os.environ['mail_password'])
class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_TLS = True
    DEBUG = False
    MAIL_USERNAME = "akwatambe3@gmail.com"
    MAIL_PASSWORD = "password"

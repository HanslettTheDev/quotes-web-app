from boto.s3.connection import S3Connection
import os

s3 = S3Connection(os.environ['SECRET_KEY'], os.environ['DATABASE_URI'], os.environ['mail_username'], os.environ['mail_password'], os.environ['PORT'])
class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = os.environ('PORT')
    MAIL_USE_TLS = True
    MAIL_USE_TLS = True 
    MAIL_USERNAME = os.environ.get('mail_username')
    MAIL_PASSWORD = os.environ.get('mail_password')
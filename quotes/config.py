# from boto.s3.connection import S3Connection
# from dotenv import load_dotenv
import os

# load_dotenv()
# s3 = S3Connection(os.environ['SECRET_KEY'], os.environ['DATABASE_URI'], os.environ['mail_username'], os.environ['mail_password'])
class Config():
    SECRET_KEY = os.getenv("SECRET_KEY") 
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") 
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    MAIL_USE_TLS = True
    MAIL_USE_TLS = True
    DEBUG = False
    MAIL_USERNAME = "akwatambe3@gmail.com"
    MAIL_PASSWORD = "password"

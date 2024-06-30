# from boto.s3.connection import S3Connection
# from dotenv import load_dotenv
import os

# load_dotenv()
# s3 = S3Connection(os.environ['SECRET_KEY'], os.environ['DATABASE_URI'], os.environ['mail_username'], os.environ['mail_password'])
class Config():
    SECRET_KEY = "Kdskkdsdfsdsdsdfsf2392342423;2=34324234" 
    SQLALCHEMY_DATABASE_URI = "postgres://koyeb-adm:vXV8tzaI4KQr@ep-yellow-term-a2f230oc.eu-central-1.pg.koyeb.app/koyebdb"
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MAIL_USE_TLS = True
    MAIL_USE_TLS = True
    DEBUG = False
    MAIL_USERNAME = "akwatambe3@gmail.com"
    MAIL_PASSWORD = "password"

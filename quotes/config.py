import os

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = "postgres://jyvgdxszsixpex:32df55c7784f8b768ab7ef830111f3a0d67b7a016a88c66954b442bf71eff418@ec2-52-2-118-38.compute-1.amazonaws.com:5432/d5nb51q2j1jp7b"
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_TLS = True 
    MAIL_USERNAME = os.environ.get('mail_username')
    MAIL_PASSWORD = os.environ.get('mail_password')
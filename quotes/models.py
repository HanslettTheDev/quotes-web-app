from datetime import datetime
from quotes import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader

def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    profile_pic = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    quote = db.relationship('Quotes', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Quotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quote = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"Quotes('{self.name}', '{self.date_posted}')"
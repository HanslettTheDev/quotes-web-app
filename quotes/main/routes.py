from flask import Blueprint, render_template, request
from quotes.models import Quotes


main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)#if the someone tries to use any other data type apart from an int it will throw an error
    posts = Quotes.query.order_by(Quotes.date_posted.desc()).paginate(page=page, per_page=6)
    return render_template('index.html', posts=posts)
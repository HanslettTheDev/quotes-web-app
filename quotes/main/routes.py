from flask import Blueprint, render_template, request, url_for, redirect
from quotes.models import Quotes
from quotes.main.forms import CategoryForm


main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home", methods=['GET', 'POST'])
def home():
    page = request.args.get('page', 1, type=int)#if the someone tries to use any other data type apart from an int it will throw an error
    posts = Quotes.query.order_by(Quotes.date_posted.desc()).paginate(page=page, per_page=20)
    form = CategoryForm()
    return render_template('index.html', form=form, posts=posts)
from flask import Blueprint, flash, redirect, url_for, render_template
from quotes.models import Quotes
from quotes.quotes_posts.forms import PostForm
from flask_login import login_required, current_user
from quotes import db 

quotes_post = Blueprint('quotes_post', __name__)

@quotes_post.route("/post/new", methods=['GET', 'POST'])
@login_required
def createpost():
    form = PostForm()
    if form.validate_on_submit():
        post = Quotes(quote=form.quote.data, category=form.category.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your Quote has been posted', 'success')
        return redirect(url_for("main.home"))
    return render_template('post.html', title='New Quote Post', form=form, legend='New Quote Post')


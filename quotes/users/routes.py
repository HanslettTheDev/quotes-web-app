from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import current_user
from quotes import db, bcrypt
from quotes.models import Quotes, Users
from quotes.users.forms import (RegistrationForm, LoginForm, 
                UpdateAccountForm, RequestResetPasswordForm, ResetPasswordForm)
from flask_login import login_user, current_user, logout_user, login_required
from quotes.users.utils import save_pic, send_reset_email

users = Blueprint('users', __name__)

@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Failed. Please Check Email And Password Fields', 'danger')
    return render_template('login.html', form=form, title='Login')

@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash("Please log out to create another account", "danger")
        return redirect(url_for("main.home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Users(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!. Log In With Your Newly Created Account', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form, title='Register')
     
@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@users.route("/my_account", methods=['GET', 'POST'])
@login_required 
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.pic.data:
            picture_file = save_pic(form.pic.data)
            current_user.profile_pic = picture_file
        current_user.username = form.username.data 
        current_user.email = form.email.data 
        db.session.commit()
        flash('Your account has been Updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method ==  'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_images/' + current_user.profile_pic)
    return render_template('account.html', title='Account', image_file=image_file, form=form)

@users.route("/user/<string:username>")
def users_quotes(username):
    page = request.args.get('page', 1, type=int)#if the someone tries to use any other data type apart from an int it will throw an error
    user = Users.query.filter_by(username=username).first_or_404()
    posts = Quotes.query.filter_by(author=user)\
        .order_by(Quotes.date_posted.desc())\
        .paginate(page=page, per_page=15)
    return render_template('users_quotes.html', posts=posts, user=user)

@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = RequestResetPasswordForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash("An email has been sent with instructions to reset your account", 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)

@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    user = Users.verify_reset_token(token)
    if user is None:
        flash('Your token is either invalid or expired', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your account has been updated! You can now log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)
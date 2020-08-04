import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from quotes import app, db, bcrypt
from quotes.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from quotes.models import Users, Quotes
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/home")
def home():
    posts = Quotes.query.all()
    return render_template('index.html', posts=posts)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Failed. Please Check Email And Password Fields', 'danger')
    return render_template('login.html', form=form, title='Login')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash("Please log out to create another account", "danger")
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Users(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!. Log In With Your Newly Created Account', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title='Register')
    

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_pic(form_pic):
    random_hex_name = secrets.token_hex(8) #create a random hex 8 digit name which will be used as a file name to avoid conflicts in the database
    _, file_ext = os.path.splitext(form_pic.filename) #create a variable using the os path split text function split the file name from the extension
    picture_name = random_hex_name + file_ext #now concactinate the random_hex_name with the file extension
    picture_path = os.path.join(app.root_path, 'static/profile_images', picture_name) #using the os module join the path of the directory of the saved file with the new concactinated variable
    # resize picture 
    final_size = (125, 125)
    i = Image.open(form_pic)
    i.thumbnail(final_size)
    
    i.save(picture_path) #use the save function to store the picture name finally
    
    return picture_name


@app.route("/Account", methods=['GET', 'POST'])
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
        return redirect(url_for('account'))
    elif request.method ==  'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_images/' + current_user.profile_pic)
    return render_template('account.html', title='Account', image_file=image_file, form=form)

@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def createpost():
    form = PostForm()
    if form.validate_on_submit():
        post = Quotes(quote=form.quote.data, category=form.category.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your Quote has been posted', 'success')
        return redirect(url_for("home"))
    return render_template('post.html', title='New Quote Post', form=form)


@app.route("/quotes_manager")
@login_required
def quotes_manager():
    posts = Quotes.query.all() 
    if current_user.is_authenticated:
        return render_template('manager.html', posts=posts, title='Post Manager')
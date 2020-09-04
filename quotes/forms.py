from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, length, Email, EqualTo, ValidationError
from quotes.models import Users

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), length(min=4, max=20)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

	def validate_username(self, username):
		user = Users.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('Sorry, username is already taken. Please chose a diffrent one')
	def validate_email(self, email):
		email = Users.query.filter_by(email=email.data).first()
		if email:
			raise ValidationError('Sorry, email is already taken. Please chose a diffrent one')

class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    pic = FileField('Change Profile Picture', validators=[FileAllowed(['jpg', 'png'], 'Images Only => Jpg, png formats only')])
    submit = SubmitField('Update')
def validate_username(self, username):
	if username.data != current_user.username:
		user = Users.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('Sorry, username is already taken. Please chose a diffrent one')
def validate_email(self, email):
	if email.data != current_user.email:
		email = Users.query.filter_by(email=email.data).first()
		if email:
			raise ValidationError('Sorry, email is already taken. Please chose a diffrent one')

class PostForm(FlaskForm):
	quote = TextAreaField("Your Quote", validators=[DataRequired()], id=['exampleFormControlTextarea1'])
	category = SelectField(u"Quote Category", validators=[DataRequired()], choices=[('#motivational'), ('#inspirational'), ('#love'), ('#social'), ('#science'), ('#didyouknow'), ('#fact')])
	submit = SubmitField('Post')
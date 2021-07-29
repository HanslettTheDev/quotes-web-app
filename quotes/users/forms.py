from flask_wtf import FlaskForm
from flask_login import current_user
from quotes.models import Users
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, ValidationError, length

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


class RequestResetPasswordForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	submit = SubmitField('Request To Reset Password')

	def validate_email(self, email):
		user = Users.query.filter_by(email=email.data).first()
		if user is None:
			raise ValidationError('Email does not exit! Please check your email or Sign up for an account')


class ResetPasswordForm(FlaskForm):
	password = PasswordField("Password", validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Reset Password')
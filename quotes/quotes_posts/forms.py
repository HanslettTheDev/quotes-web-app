from flask_wtf import FlaskForm
from wtforms import TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
	quote = TextAreaField("Your Quote", validators=[DataRequired()], id=['exampleFormControlTextarea1'])
	category = SelectField(u"Quote Category", validators=[DataRequired()], choices=[('#motivational'), 
	('#inspirational'), ('#love'), ('#social'), 
	('#science'), ('#didyouknow'), ('#fact')])
	submit = SubmitField('Post')


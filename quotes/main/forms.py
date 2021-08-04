from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

class CategoryForm(FlaskForm):
    category = SelectField(u"Choose a category to filter", validators=[DataRequired()], choices=[('#motivational'),('#inspirational'), ('#love'), 
    ('#social'),('#science'), ('#didyouknow'), ('#fact')])
    filter_button = SubmitField('Filter')
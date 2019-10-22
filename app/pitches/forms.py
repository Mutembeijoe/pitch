from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    category = SelectField(u'Category', choices=[('tech', 'Technology'), ('physics', 'Physics'), ('environment', 'Environment')]
                           ,validators=[DataRequired()])
    submit = SubmitField('Post')


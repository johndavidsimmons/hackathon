from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, DateField
from wtforms.validators import Required

class surveyForm(FlaskForm):
    surveyName = StringField('Survey Name: ', validators=[Required()])
    submit = SubmitField('Next')

class respondersForm(FlaskForm):
    responders = StringField('Who is this survey being sent to? ')
    submit = SubmitField('Next')


from flask_wtf import FlaskForm
from wtforms.fields import StringField, DateField, IntegerField, RadioField
from wtforms.validators import Required

class surveyForm(FlaskForm):
    surveyName = StringField('Survey Name: ', validators=[Required()])
    responseLimit = IntegerField('How many times can users respond? ',validators=[Required()])
    publicSurvey = RadioField('Is this survey public or private? ',
                              choices=[('Yes', 'Yes'), ('No', 'No')],
                              validators=[Required()])


class respondersForm(FlaskForm):
    responders = StringField('Who is this survey being sent to? ')


class questionForm(FlaskForm):
    questionText = StringField('Add your first question: ', validators=[Required()])


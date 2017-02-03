from flask_wtf import FlaskForm
from wtforms.fields import StringField, DateField, IntegerField, RadioField
from wtforms import validators

class surveyForm(FlaskForm):
    surveyName = StringField('Survey Name: ', [validators.DataRequired()])
    responseLimit = IntegerField('How many times can users respond? ',[validators.DataRequired()])
    publicSurvey = RadioField('Is this survey public or private? ',
                              choices=[('Yes', 'Yes'), ('No', 'No')])


class respondersForm(FlaskForm):
    responders = StringField('Who is this survey being sent to? ')
    skills = StringField('People who are good at...')
    interests = StringField('People who are interested in...')
    location = StringField('People who who sit in...')
    tms = StringField('My Team ')


class questionForm(FlaskForm):
    questionText = StringField('Add your question: ', [validators.Required()])
    completeSurvey = RadioField(choices=[('Yes', 'Yes'), ('No', 'No')])


class choiceForm(FlaskForm):
    choiceText = StringField('Add response choice: ', [validators.Required()])
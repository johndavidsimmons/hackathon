import os
from flask import Flask, render_template, redirect, url_for
from . import main
from flask_security import login_required, current_user
from flask import request
from .. import databaseModels as dm
from forms import surveyForm, respondersForm, questionForm
import datetime


@main.route("/")
def index():
    return render_template("index.html")


@main.route('/createSurvey/', methods=['GET', 'POST'])
def createSurvey():

    # if user is submitting form
    if request.form:
        surveyName = request.form.get('surveyName')
        surveyCreateDt = datetime.datetime.now()
        responseLimit = request.form.get('responseLimit')
        creatorID = ''
        if request.form.get('publicSurvey') == 'Yes':
            public = True
        else:
            public = False

        b = dm.surveyModel(surveyName=surveyName,
                           surveyCreateDt=surveyCreateDt,
                           responseLimit=responseLimit,
                           creatorID=creatorID,
                           publicSurvey=public)
        dm.db_session.add(b)
        # dm.db_session.commit()
        return redirect(url_for('main.addResponders'))

    # if users has not yet submitted form
    form = surveyForm()
    return render_template('surveyName.html', form=form)


@main.route('/addResponders/', methods=['GET', 'POST'])
def addResponders():
    if request.form:
        responders = request.form.get("responders")
        # b = dm.surveyModel()
        # dm.db_session.add(b)
        # dm.db_session.commit()
        return redirect(url_for('main.addQuestion'))
    form = respondersForm()
    return render_template('addResponders.html', form=form)


@main.route('/addQuestion/', methods=['GET', 'POST'])
def addQuestion():
    if request.form:
        questionText = request.form.get("questionText")
        # b = dm.questionModel()
        # dm.db_session.add(b)
        # dm.db_session.commit()
        return redirect(url_for('main.Answers'))
    form = questionForm()
    return render_template('addQuestions.html', form=form)






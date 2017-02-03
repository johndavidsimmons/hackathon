import os
from flask import Flask, render_template, redirect, url_for
from . import main
from flask_security import login_required, current_user
from flask import request
from .. import databaseModels as dm
from forms import surveyForm

@main.route("/")
def index():
	return render_template("index.html")

@main.route('/createSurvey/')
def createSurvey():

    # if user is submitting form
    if request.form:
        surveyName = request.form.get('surveyName')
        b = dm.surveyModel(surveyName)
        dm.db_session.add(b)
        dm.db_session.commit()
        return redirect(url_for('responders'))

    #if users has not yet submitted form
    form = surveyForm()
    return render_template('surveyName.html', form=form)

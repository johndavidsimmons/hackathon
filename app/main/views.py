import os
from flask import Flask, render_template, redirect, url_for
from . import main
from flask_security import login_required, current_user
from flask import request
from .. import databaseModels as dm
from forms import surveyForm, respondersForm, questionForm, choiceForm
import datetime
#from querying import audience
import sqlite3

siid = None
qiid = None

def audience(choiceID, str=''):
  conn = sqlite3.connect(r"C:\Users\nhounshell\Documents\github\hackathon\data-dev.sqlite")

  c = conn.cursor()
  queries = {0: "select distinct Name from floorData where DisplayName like ?"
            ,1: 'select distinct Name from skill_mapping where skill like ?'
            ,2: 'select distinct Name from interest_mapping where interest like ?'
            ,3: 'select distinct Name from team_breakout where team == "BI IQ"'
            }
  if choiceID < 3:
      c.execute(queries[choiceID], ["%"+str+"%"])
  else:
      c.execute(queries[3])

  return [x[0] for x in c.fetchall()]


@main.route("/")
def index():
    if current_user.is_authenticated:
       email = current_user.email
    else:
       email=None
    u = dm.User.query.filter_by(email=email).first()
    return render_template("index.html", u=u)


@main.route("/myDash/")
def myDash():
    if current_user.is_authenticated:
       email = current_user.email
    else:
       email=None
    u = dm.User.query.filter_by(email=email).first()


    return render_template("myDash.html", u=u)


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
        dm.db_session.commit()

        surveyKey = dm.surveyModel.query.filter_by(surveyName=surveyName, surveyCreateDt=surveyCreateDt).first()
        global siid 
        siid = surveyKey.surveyID
        return redirect(url_for('main.addResponders'))

    # if users has not yet submitted form
    form = surveyForm()
    return render_template('surveyName.html', form=form)


@main.route('/addResponders/', methods=['GET', 'POST'])
def addResponders():
    if request.form:
        location = request.form.get("location")
        skills = request.form.get("skills")
        interests = request.form.get("interests")
        print location, skills, interests
        if location: print audience(0, location)
        if skills: print audience(1, skills)
        if interests: print audience(2, interests)
        return redirect(url_for('main.addResponders'))
    form = respondersForm()
    return render_template('addResponders.html', form=form)


@main.route('/addQuestion/', methods=['GET', 'POST'])
def addQuestion():
    if request.form:
        questionText = request.form.get("questionText")
        b = dm.questionModel(questionText=questionText, survey_ID=siid)
        dm.db_session.add(b)
        dm.db_session.commit()

        questionKey = dm.questionModel.query.filter_by(questionText=questionText).first()
        global qiid
        qiid = questionKey.questionID

        return redirect(url_for('main.addChoices'))
    form = questionForm()
    return render_template('addQuestions.html', form=form)


@main.route('/addChoices/', methods=['GET', 'POST'])
def addChoices():
    if request.form:
        choiceText = request.form.get('choiceText')
        b = dm.choiceModel(question_ID=qiid, surveyID=siid, choiceText=choiceText)
        dm.db_session.add(b)
        dm.db_session.commit()
        return redirect(url_for('main.addChoices'))
    form = choiceForm()
    return render_template('choiceForm.html', form=form)

@main.route('/approval/')
def approval():
    recipients = ['JasonCharles@quickenloans.com','RuthLincoln@quickenloans.com','JohnSimmons@quickenloans.com']
    questions = ['Where should we go to lunch today?', 'What time works best?']
    return render_template('approvalTemplate.html', questions=questions, recipients=recipients)

@main.route('/thankYou/')
def thankYou():
    return render_template('thankYou.html')

@main.route('/snacks/')
def snacks():
    return render_template('snacks.html')


@main.route("/myDash1/")
def myDash1():
    if current_user.is_authenticated:
       email = current_user.email
    else:
       email=None
    u = dm.User.query.filter_by(email=email).first()


    return render_template("myDash1.html", u=u)









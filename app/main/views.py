import os
from flask import Flask, render_template, request, redirect, url_for
from . import main
from flask_security import login_required, current_user
from ..databaseModels import *


@main.route("/")
def index():

	email = current_user.email
	u = User.query.filter_by(email=email).first()
	return render_template("index.html", u=u)
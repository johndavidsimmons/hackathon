import os
from flask import Flask, render_template
from . import main
from flask_security import login_required, current_user


@main.route("/")
def index():
	return render_template("index.html")


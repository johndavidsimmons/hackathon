from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_script import Manager
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required, current_user
import pandas as pd

manager = Manager()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # ############################## flask-security ##########################
    # create database connection
    db1 = SQLAlchemy(app)

    # define models
    roles_users = db1.Table('roles_users',
                    db1.Column('user_id', db1.Integer(), db1.ForeignKey('user.id')),
                    db1.Column('role_id', db1.Integer(), db1.ForeignKey('role.id')))


    class Role(db1.Model, RoleMixin):
        id = db1.Column(db1.Integer, primary_key=True)
        name = db1.Column(db1.String(80), unique=True)
        description = db1.Column(db1.String(225))


    class User(db1.Model, UserMixin):
        id = db1.Column(db.Integer, primary_key=True)
        email = db1.Column(db1.String(255), unique=True)
        password = db1.Column(db1.String(255))
        active = db1.Column(db1.Boolean())
        confirmed_at = db1.Column(db1.DateTime())
        roles = db1.relationship('Role', secondary=roles_users,
                                backref=db1.backref('users', lazy='dynamic'))

    # Setup Flask-Security
    user_datastore = SQLAlchemyUserDatastore(db1, User, Role)
    security = Security(app, user_datastore)



    # Create a user to test with
    # @app.before_first_request
    # def create_user():

    #     file = pd.read_csv('logins.csv')
    #     for i,r in file.iterrows():
    #         print r.email
    #         db1.create_all()
    #         user_datastore.create_user(email=r.email, password=r.extension)
    #         db1.session.commit()

    # ############################## end flask-security #######################

    return app
# Imports
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

# Environmental configs
if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///plants.db"
    app.config["SQLALCHEMY_ECHO"] = True

# This is the object that we're importing everywhere and issuing commands to
db = SQLAlchemy(app)

# adress space
from application import views
from application.auth import views
from application.data.plants import views

# database tables
from application.data.plants import models
from application.auth import models 

# login functionality
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "You need to be logged in to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Create all tables
db.create_all()
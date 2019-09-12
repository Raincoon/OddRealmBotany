# Initialise Flask
from flask import Flask
app = Flask(__name__)

# Initialise SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Configs for SQLAlchemy
#  database to be used
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///plants.db"
#  log all statements to stderr
app.config["SQLALCHEMY_ECHO"] = True

# This is the object that we're importing everywhere and issuing commands to
db = SQLAlchemy(app)

from application import views

from application.data import models

# Create all tables
db.create_all()
from flask_wtf import FlaskForm
from wtforms import validators, PasswordField, StringField, SubmitField
  
class LoginForm(FlaskForm):
    username = StringField("Username",[validators.required()])
    password = PasswordField("Password", [validators.required()])
    button = SubmitField("Log In") # default value, replaced when using the form to sign up

    class Meta:
        csrf = False

# TO DO- a separate signup form with stricter field lengths
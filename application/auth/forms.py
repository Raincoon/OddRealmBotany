from flask_wtf import FlaskForm
from wtforms import validators, PasswordField, StringField, SubmitField
  
class LoginForm(FlaskForm):
    username = StringField("Username",[validators.required()])
    password = PasswordField("Password", [validators.required()])
    button = SubmitField("Log In")

    class Meta:
        csrf = False

class SignupForm(FlaskForm):
    username = StringField("Username",[
        validators.required(),
        validators.Length(min=2,max=25)])
    password = PasswordField("Password", [
        validators.required(),
        validators.Length(min=4,max=80)])
    button = SubmitField("Sign Up")

    class Meta:
        csrf = False
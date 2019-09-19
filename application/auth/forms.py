from flask_wtf import FlaskForm
from wtforms import validators, PasswordField, StringField
  
class LoginForm(FlaskForm):
    username = StringField("Username",[validators.required()])
    password = PasswordField("Password", [validators.required()])
  
    class Meta:
        csrf = False
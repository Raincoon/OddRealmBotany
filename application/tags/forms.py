from flask_wtf import FlaskForm
from wtforms import validators, StringField, SubmitField

class TagForm(FlaskForm):
    name = StringField("Tag text", [
        validators.required(), 
        validators.Length(min=3,max=20)])
    button = SubmitField("Add")

    class Meta:
        csrf = False
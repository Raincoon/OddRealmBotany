from flask_wtf import FlaskForm
from wtforms import validators, StringField

class TagForm(FlaskForm):
    name = StringField("Tag", [
        validators.required(), 
        validators.Length(max=50)])

    class Meta:
        csrf = False
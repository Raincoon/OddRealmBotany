from flask_wtf import FlaskForm
from wtforms import validators, StringField, IntegerField, BooleanField, SelectField

class PlantForm(FlaskForm):
    name = StringField("Name", [
        validators.required(), 
        validators.Length(max=20)])
    mature_time = IntegerField("Mature Time", [
        validators.NumberRange(min=1, max=9000),
        validators.required()])
    is_tree = BooleanField("is_tree")

    class Meta:
        csrf = False

class PlantTagForm(FlaskForm):
    taglist = SelectField("Tag list", [validators.required()])

    class Meta:
        csrf = False

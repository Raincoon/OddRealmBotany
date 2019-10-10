from flask_wtf import FlaskForm
from wtforms import validators, StringField, IntegerField, BooleanField, SelectField, SubmitField

class PlantForm(FlaskForm):
    name = StringField("Name", [
        validators.required(), 
        validators.Length(min=3,max=20)])
    mature_time = IntegerField("Mature Time", [
        validators.NumberRange(min=1, max=120),
        validators.required(message="A number input between 0 and 120 is required")])
    is_tree = BooleanField("is_tree")
    button = SubmitField("Submit") # default value, replaced when using the form for plant editing

    class Meta:
        csrf = False

class PlantTagForm(FlaskForm):
    taglist = SelectField("Select a Tag", [validators.required()])
    button = SubmitField("Add")

    class Meta:
        csrf = False

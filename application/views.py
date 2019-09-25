from flask import render_template, redirect, url_for
from flask_login import current_user

from application import app, db
from application.plants.models import Plant

# landing page,
@app.route("/", methods=["GET"])
def index():

    if current_user.is_authenticated:
        return redirect(url_for("plant_list"))
    else:
        return render_template("index.html")

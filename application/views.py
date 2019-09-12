from flask import redirect, render_template, request, url_for
from application import app, db
from application.data.models import Plant

@app.route("/", methods=["GET"])
def index():
    return render_template("plant_list.html", plants = Plant.query.all())

@app.route("/new_plant")
def new_plant():
    return render_template("new_plant.html")

@app.route("/plants/", methods=["POST"])
def plant_create():
    name = request.form.get("name")
    hrs = request.form.get("grow_time_hrs")
    tree = False
    if request.form.get("is_tree") == 'on' : tree = True

    t = Plant(name, hrs, tree)

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("index"))
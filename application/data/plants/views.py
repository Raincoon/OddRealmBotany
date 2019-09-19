from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.data.plants.models import Plant
from application.data.plants.forms import PlantForm

# plant list of user's plants
@app.route("/garden", methods=["GET"])
@login_required
def plant_list():
    return render_template("plant_list.html", plants = Plant.query.filter_by(owner_id=current_user.id))

# page for plant creation form
@app.route("/add_plant")
@login_required
def new_plant():
    return render_template("new_plant.html", form = PlantForm())

# adding a plant entry
@app.route("/plants/", methods=["POST"])
@login_required
def plant_create():
    form = PlantForm(request.form)

    if not form.validate():
        return render_template("new_plant.html", form = form)

    name = form.name.data
    hrs = form.mature_time.data
    tree = form.is_tree.data

    # create plant entry and save to database
    p = Plant(name, hrs, tree)
    p.owner_id = current_user.id

    db.session().add(p)
    db.session().commit()
  
    return redirect(url_for("plant_list"))

# modifying a plant entry TBA

# removing a plant entry
@app.route("/plants/remove/<remove_id>/", methods=["POST"])
@login_required
def plant_remove(remove_id):

    p = Plant.query.get(remove_id)
    db.session().delete(p)
    db.session().commit()
  
    return redirect(url_for("plant_list"))
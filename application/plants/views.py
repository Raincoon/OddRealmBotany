from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.plants.models import Plant
from application.plants.forms import PlantForm

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

# modifying a plant entry
@app.route("/plants/<edit_id>", methods=["GET","POST"])
@login_required
def plant_edit(edit_id):
    p = Plant.query.get(edit_id)
    if request.method == "GET":
        return render_template("edit_plant.html", plant=p, form = PlantForm(obj=p))

    form = PlantForm(request.form)
    if not form.validate():
            return render_template("edit_plant.html", plant=p, form = form)

    
    name = form.name.data
    hrs = form.mature_time.data
    tree = form.is_tree.data

    p.name = name
    p.mature_time = hrs
    p.is_tree = tree

    db.session().commit()
    return redirect(url_for("plant_list"))




# removing a plant entry
@app.route("/plants/remove/<remove_id>/", methods=["POST"])
@login_required
def plant_remove(remove_id):

    p = Plant.query.get(remove_id)
    db.session().delete(p)
    db.session().commit()
  
    return redirect(url_for("plant_list"))
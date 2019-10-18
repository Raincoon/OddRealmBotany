from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.plants.models import Plant
from application.plants.forms import PlantForm, PlantTagForm
from application.tags.models import Tag

# list of all user's plants
@app.route("/garden", methods=["GET"])
@login_required
def plant_list():

    plants = Plant.query.filter_by(owner_id=current_user.id)
    plantcount = Plant.count_plants_from_user(current_user.id)

    return render_template("plants/plant_list.html", plants = plants, count = plantcount)

# adding a plant entry
@app.route("/plants/new", methods=["GET","POST"])
@login_required
def plant_new():

    if request.method == "GET":
        return render_template("plants/plant_new.html", form=PlantForm())

    form = PlantForm(request.form)

    if not form.validate():
        return render_template("plants/plant_new.html", form=form)

    name = form.name.data
    hrs = form.mature_time.data
    tree = form.is_tree.data

    # creating the plant
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
        # populating the form, changing button text
        _form = PlantForm(obj=p)
        _form.button.label.text = "Edit"
        
        return render_template("plants/plant_edit.html", plant=p, form=_form)

    form = PlantForm(request.form)
    if not form.validate():
            return render_template("plants/plant_edit.html", plant=p, form=form)

    name = form.name.data
    hrs = form.mature_time.data
    tree = form.is_tree.data

    # making the edits
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
    return redirect(url_for("index"))

# tagging a plant
@app.route("/plants/tag/<plant_id>", methods=["GET","POST"])
@login_required
def plant_tag(plant_id):
    p = Plant.query.get(plant_id)
    form = PlantTagForm()
    tags = Tag.query.filter_by(owner_id=current_user.id)
    tag_list = [(tag.id, tag.name) for tag in tags]

    if request.method == "GET":
        form.taglist.choices = tag_list
        return render_template("plants/plant_tag.html",plant=p, form=form)
    
    form = PlantTagForm(request.form)
    tag_id = form.taglist.data

    t = Tag.query.get(tag_id)

    # add the tag
    p.tags.append(t)
    db.session().commit()
    return redirect(url_for("plant_list"))

# un-tagging a plant
@app.route("/plants/untag/<plant_id>", methods=["GET","POST"])
@login_required
def plant_untag(plant_id):
    p = Plant.query.get(plant_id)
    form = PlantTagForm()
    tags = p.tags
    tag_list = [(tag.id, tag.name) for tag in tags]

    if request.method == "GET":
        form.taglist.choices = tag_list
        # changing button text
        form.button.label.text = "Remove"
        return render_template("plants/plant_untag.html",plant=p, form=form)

    form = PlantTagForm(request.form)
    tag_id = form.taglist.data
    t = Tag.query.get(tag_id)

    # remove the tag
    p.tags.remove(t)
    db.session().commit()
    return redirect(url_for("plant_list"))
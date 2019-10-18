from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.tags.models import Tag
from application.tags.forms import TagForm
from application.plants.models import Plant

# list plants under a specific tag
@app.route("/tags/<tag_id>", methods=["GET"])
@login_required
def tag_list(tag_id):

    t = Tag.query.get(tag_id)

    # filter plants that have been tagged
    plants = Plant.query.filter_by(owner_id=current_user.id).filter(Plant.tags.any(Tag.id == tag_id))

    return render_template("tags/tag_list.html", plants=plants, tag=t)


# add a tag
@app.route("/tags/", methods=["GET","POST"])
@login_required
def tag_new():

    # forms
    if request.method == "GET":
        return render_template("tags/tag_new.html", form=TagForm())
    
    form = TagForm(request.form)
    if not form.validate():
        return render_template("tags/tag_new.html", form=form)

    name = form.name.data

    # creating the tag
    t = Tag(name)
    t.owner_id = current_user.id

    db.session().add(t)
    db.session().commit()
    return redirect(url_for("index"))

#edit a tag
@app.route("/tags/edit/<edit_id>", methods=["GET","POST"])
@login_required
def tag_edit(edit_id):

    t = Tag.query.get(edit_id)

    if request.method == "GET":
        # populating form, changing button text
        _form = TagForm(obj=t)
        _form.button.label.text = "Edit"

        return render_template("tags/tag_edit.html", form=_form, tag=t)

    form = TagForm(request.form)
    if not form.validate():
        return render_template("tags/tag_edit.html", form=form, tag=t)
    
    name = form.name.data
    
    # making the edits
    t.name = name
    
    db.session().commit()
    return redirect(url_for("index"))

# remove a tag
@app.route("/tags/remove/<remove_id>/", methods=["POST"])
@login_required
def tag_remove(remove_id):

    t = Tag.query.get(remove_id)

    db.session().delete(t)
    db.session().commit()
    return redirect(url_for("index"))
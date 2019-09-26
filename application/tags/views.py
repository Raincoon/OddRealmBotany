from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.tags.models import Tag
from application.tags.forms import TagForm

# Add a tag
@app.route("/tags/", methods=["GET","POST"])
@login_required
def tag_new():

    # forms
    if request.method == "GET":
        return render_template("tag_new.html", form=TagForm())
    
    form = TagForm(request.form)
    if not form.validate():
        return render_template("tag_new.html", form=form)

    name = form.name.data

    # creating the tag
    t = Tag(name)
    t.owner_id = current_user.id

    db.session().add(t)
    db.session().commit()
    return redirect(url_for("index"))

# Edit a tag
@app.route("/tags/edit/<edit_id>", methods=["GET","POST"])
@login_required
def tag_edit(edit_id):

    t = Tag.query.get(edit_id)
    if request.method == "GET":
        return render_template("tag_edit.html", form=TagForm(obj=t))

    form = TagForm(request.form)
    if not form.validate():
        return render_template("tag_edit.html", form=form)
    
    name = form.name.data
    
    # making the edits
    t.name = name
    
    db.session().commit()
    return redirect(url_for("index"))

# Remove a tag
@app.route("/tags/remove/<remove_id>/", methods=["POST"])
@login_required
def tag_remove(remove_id):

    t = Tag.query.get(remove_id)

    db.session().delete(t)
    db.session().commit()
    return redirect(url_for("index"))
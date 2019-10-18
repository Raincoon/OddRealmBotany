from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application import bcrypt
from application.auth.models import User
from application.auth.forms import LoginForm, SignupForm

# Adding new user accout
@app.route("/auth/register", methods = ["GET", "POST"])
def auth_new_user():
    
    if request.method == "GET":
        return render_template("auth/registerform.html", form=SignupForm())
    
    form = SignupForm(request.form)
    if not form.validate():
        return render_template("auth/registerform.html", form=form)

    # get form data and hash password
    uname = form.username.data
    pw = bcrypt.generate_password_hash(form.password.data, 13).decode("utf-8")

    # check if username is available
    user = User.query.filter_by(username=uname).first()
    if not user:
        # create user account entry and save to database
        a = User(uname, pw)

        db.session().add(a)
        db.session().commit()

        return redirect(url_for("auth_login"))
    else:
        return render_template("auth/registerform.html", form = form, 
                                error = "Please select another username")



# Logging in
@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    if not form.validate():
        return render_template("auth/loginform.html", form = form)

    # get data from LoginForm
    uname = form.username.data
    pw = form.password.data

    # find user and check credentials
    user = User.query.filter_by(username=uname).first()
    if user and bcrypt.check_password_hash(user.password, pw):
        login_user(user)
        return redirect(url_for("index"))
    else:
        return render_template("auth/loginform.html", form = form, 
                                error = "Wrong username or password")

    

# Logging out
@app.route("/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))
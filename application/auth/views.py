from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
  
from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, UserForm
from application.tasks.models import Task

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                                error = "No such username or password")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/sign/")
def auth_form():
    return render_template("auth/sign.html",form = LoginForm())

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))      

@app.route("/auth/sign/", methods = ["POST"])
def auth_create():
    form = LoginForm(request.form)

    if not form.validate():
        return render_template("auth/sign.html", form = form)

    user = User(form.name.data, form.username.data, form.password.data, form.role.data)
    db.session().add(user)
    db.session().commit()

    return redirect(url_for("auth_login"))

@app.route("/auth/information/", methods = ["GET"])
@login_required
def auth_information():

    return render_template("auth/information.html", form = UserForm(), tasks = Task.find_users_tasks(current_user.id))

@app.route("/auth/information/", methods = ["POST"])
@login_required
def auth_info():

    form = UserForm(request.form)
    user = User.query.get(current_user.id)

    if not form.validate():
        return render_template("auth/information.html", form = UserForm(), tasks = Task.find_users_tasks(current_user.id))

    if form.name.data:
        user.name = form.name.data

    if form.username.data:
        if not User.unique_username(form.username.data):
            user.username = form.username.data

    if form.password.data:
        user.password = form.password.data

    db.session().commit()

    return redirect(url_for("auth_information"))
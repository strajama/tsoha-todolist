from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.tasks.models import Task
from application.tasks.forms import TaskForm

@app.route("/tasks", methods=["GET"])
def tasks_index():
    return render_template("tasks/list.html", tasks = Task.query.all(), find_user=Task.find_user(Task.account_id))

@app.route("/tasks/new/", methods=["GET"])
@login_required
def tasks_form():
    return render_template("tasks/new.html", form = TaskForm())

@app.route("/tasks/", methods=["POST"])
@login_required
def tasks_create():
    form = TaskForm(request.form)

    if not form.validate():
        return render_template("tasks/new.html", form = form)

    t = Task(form.name.data)
    t.description = form.description.data
    t.done = "kesken"
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("tasks_index"))

@app.route("/tasks/edit/<task_id>/", methods=["GET"])
@login_required
def tasks_edit(task_id):
    return render_template("tasks/edit.html", task_id = task_id, form = TaskForm(), task=Task.query.get(task_id))

@app.route("/tasks/edit/<task_id>/", methods=["POST"])
@login_required
def tasks_editor(task_id):
    form = TaskForm(request.form)
    task = Task.query.get(task_id)

    if form.name.data:
        if not form.validate():
            return render_template("tasks/new.html", form = form)
        else:
            task.name = form.name.data

    if form.description.data:
        task.description = form.description.data

    if form.done.data:
        task.done = form.done.data

    db.session().commit()

    return redirect(url_for("tasks_edit", task_id = task_id))
  
@app.route("/tasks/<task_id>/", methods=["POST"])
@login_required
def tasks_delete(task_id):
    task = Task.query.get(task_id)

    db.session.delete(task)
    db.session().commit()
  
    return redirect(url_for("tasks_index"))



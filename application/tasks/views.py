from application import app, db
from flask import redirect, render_template, request, url_for
from application.tasks.models import Task

@app.route("/tasks", methods=["GET"])
def tasks_index():
    return render_template("tasks/list.html", tasks = Task.query.all())

@app.route("/tasks/new/")
def tasks_form():
    return render_template("tasks/new.html")

@app.route("/tasks/edit/")
def tasks_edit():
    return render_template("tasks/edit.html")
  
@app.route("/tasks/<task_id>/", methods=["POST"])
def tasks_set_done(task_id):

    t = Task.query.get(task_id)
    if t.done == 0:
        t.done = 1
    else:
        t.done = 0
    db.session().commit()
  
    return redirect(url_for("tasks_index"))

@app.route("/tasks/", methods=["POST"])
def tasks_create():
    t = Task(request.form.get("name"), request.form.get("description"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("tasks_index"))

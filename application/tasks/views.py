from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required

from application import app, db
from application.tasks.models import Task
from application.tasks.forms import TaskForm
from application.tags.models import Tag
from application.auth.models import User

@app.route("/tasks", methods=["GET"])
def tasks_index():
    return render_template("tasks/list.html", tasks = Task.query.all())

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
    task = Task(form.name.data, form.description.data, form.estimated_time.data)
    task.used_time = 0
    task.account_id = current_user.id
    task.username = current_user.name

    db.session().add(task)
    db.session().commit()
  
    return redirect(url_for("tasks_index"))

@app.route("/tasks/edit/<task_id>/", methods=["GET"])
@login_required
def tasks_edit(task_id):
    return render_template("tasks/edit.html", task_id = task_id, form = TaskForm(), task=Task.query.get(task_id), tags=Tag.query.all())

@app.route("/tasks/edit/<task_id>/", methods=["POST"])
@login_required
def tasks_editor(task_id):

    form = TaskForm(request.form)
    task = Task.query.get(task_id)

    if (current_user.id != task.account_id): 
        return redirect(url_for("tasks_index"))

    if form.name.data:
        if len(form.name.data) > 30 or len(form.name.data) < 2:
            return render_template("tasks/edit.html", form = form, task_id = task_id, task=Task.query.get(task_id), tags=Tag.query.all())
        else:
            task.name = form.name.data

    if form.description.data:
        if len(form.description.data) > 60:
            return render_template("tasks/edit.html", form = form, task_id = task_id, task=Task.query.get(task_id), tags=Tag.query.all())
        else:
            task.description = form.description.data

    if form.estimated_time.data:
        if form.estimated_time.data < 1 or form.estimated_time.data > 999:
            return render_template("tasks/edit.html", form = form, task_id = task_id, task=Task.query.get(task_id), tags=Tag.query.all())
        else:
            task.estimated_time = form.estimated_time.data

    if form.used_time.data:
        if form.used_time.data < 0 or form.used_time.data > 999:
            return render_template("tasks/edit.html", form = form, task_id = task_id, task=Task.query.get(task_id), tags=Tag.query.all())
        else:
            task.used_time = form.used_time.data
            if task.used_time > task.estimated_time:
                task.estimated_time = task.used_time

    db.session().commit()

    return redirect(url_for("tasks_edit", task_id = task_id))
  
@app.route("/tasks/<task_id>/delete", methods=["POST"])
@login_required
def tasks_delete(task_id):
    print('delete')
    task = Task.query.get(task_id)

    db.session.delete(task)
    db.session().commit()
  
    return redirect(url_for("tasks_index"))

@app.route("/tasks/<task_id>/", methods=["POST"])
@login_required
def tasks_addTime(task_id):
    print('addtime')
    task = Task.query.get(task_id)
    task.used_time = task.used_time + 1
    if (task.used_time > task.estimated_time):
        task.estimated_time = task.used_time

    db.session.commit()

    return redirect(url_for("tasks_index"))

@app.route("/tasks//tasktags/<task_id>", methods=["GET"])
def tasks_tagsget(task_id):
    return render_template("tasks/tasktags.html", task_id = task_id, task=Task.query.get(task_id), tags=Tag.query.all())

@app.route("/tasks//tasktags/<task_id>", methods=["POST"])
@login_required
def tasks_tags(task_id):
    task = Task.query.get(task_id)
    tagtask = request.form.getlist('tags')

    for i in tagtask:
        tag = Tag.query.get(i)
        if tag in task.tags:
            task.tags.remove(tag)
        else:
            task.tags.append(tag)       

    db.session().commit()  

    return redirect(url_for("tasks_tagsget", task_id = task_id))
from flask import render_template
from application import app
from application.auth.models import User
from application.tags.models import Tag
from application.tasks.models import Task

@app.route("/")
def index():
    return render_template("index.html", 
            unstarted_tasks=User.find_users_with_unstarted_tasks(),
            assigned_tags=Tag.find_tags_that_assigned_task(),
            tasks_roles=User.find_number_of_tasks_by_user_roles(),
            used_tags=Tag.find_used_tags())

@app.route("/findtask")
def find_task(task_name):
    task_id = Task.find_task_id(task_name)
    returnTask = Task.query.get(task_id)
    db.session().commit()

    return render_template("index.html", 
            unstarted_tasks=User.find_users_with_unstarted_tasks(),
            assigned_tags=Tag.find_tags_that_assigned_task(),
            tasks_roles=User.find_number_of_tasks_by_user_roles(),
            used_tags=Tag.find_used_tags(), 
            return_Task = returnTask )
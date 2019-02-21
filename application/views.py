from flask import render_template
from application import app
from application.auth.models import User
from application.tags.models import Tag

@app.route("/")
def index():
    return render_template("index.html", 
            unstarted_tasks=User.find_users_with_unstarted_tasks(),
            used_tags=Tag.find_tags_that_assigned_task(),
            tasks_roles=User.find_number_of_tasks_by_user_roles(),
            most_used_tags=Tag.find_most_used_tags())
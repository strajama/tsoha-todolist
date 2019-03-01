from flask import render_template, request
from application import app
from application.auth.models import User
from application.tags.models import Tag

@app.route("/")
def index():
    return render_template("index.html", 
            unstarted_tasks=User.find_users_with_unstarted_tasks(),
            tasks_roles=User.find_number_of_tasks_by_user_roles(),
            used_tags=Tag.find_used_tags())
  
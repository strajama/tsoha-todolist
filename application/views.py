from flask import render_template
from application import app
from application.auth.models import User
from application.tags.models import Tag

@app.route("/")
def index():
    return render_template("index.html", 
            needs_tasks=User.find_users_with_no_tasks(), 
            unfinished_tasks=User.find_users_with_unfinished_tasks(),
            used_tags=Tag.find_tags_that_assigned_task())
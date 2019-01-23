from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class TaskForm(FlaskForm):
    name = StringField("Task name", [validators.Length(min=2)])
    description = StringField("Description")
    done = IntegerField("Done")
 
    class Meta:
        csrf = False


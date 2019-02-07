from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class TaskForm(FlaskForm):
    name = StringField("Task name", [validators.Length(min=2, max=144)])
    description = StringField("Description", [validators.Length( max=144)])
    done = StringField("Done", [validators.Length( max=144)])
 
    class Meta:
        csrf = False


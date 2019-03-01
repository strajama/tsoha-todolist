from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators
from application.tags.models import Tag

class TaskForm(FlaskForm):
    name = StringField('Task name', [validators.Length(min=2, max=30)])
    description = StringField('Description', [validators.Length( max=60)])
    estimated_time = IntegerField('Estimated time', [validators.NumberRange(min=1, max=999)])
    used_time = IntegerField('Time used')
 
    class Meta:
        csrf = False

    def edit_tags(self):
        TaskForm.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by('name')]

class EditTaskForm(FlaskForm):
    name = StringField('Task name', [validators.Length(min=2, max=30), validators.Optional()])
    description = StringField('Description', [validators.Length( max=60), validators.Optional()])
    estimated_time = IntegerField('Estimated time', [validators.NumberRange(min=1, max=999), validators.Optional()])
    used_time = IntegerField('Time used', [validators.NumberRange(min=0, max=999), validators.Optional()])
 
    class Meta:
        csrf = False
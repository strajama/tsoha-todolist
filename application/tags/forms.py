from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError
from application.tags.models import Tag

def validate_tagname(form, field):
    if Tag.query.filter_by(name = field.data).count():
        raise ValidationError('This tag already exists.')

class TagForm(FlaskForm):
    name = StringField("Tag name", [validators.Length(min=2, max=30), validate_tagname])
 
    class Meta:
        csrf = False

class EditTagForm(FlaskForm):
    name = StringField("Tag name", [validators.Optional(), validators.Length(min=2, max=30)])
 
    class Meta:
        csrf = False
from flask_wtf import FlaskForm
from wtforms import StringField, validators

class TagForm(FlaskForm):
    name = StringField("Tag name", [validators.Length(min=2)])
 
    class Meta:
        csrf = False
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SelectMultipleField, validators

class TaskForm(FlaskForm):
    name = StringField('Task name', [validators.Length(min=2, max=144)])
    description = StringField('Description', [validators.Length( max=1000)])
    estimatedtime = DecimalField('Estimated time', [validators.NumberRange(min=1, max=999)])
    usedtime = DecimalField('Time used')
    tags = SelectMultipleField(u'Tags', coerce=int)
 
    class Meta:
        csrf = False


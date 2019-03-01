from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField, validators, ValidationError
from flask_login import current_user
from application.auth.models import User

def validate_first_username(form, field):
    if not current_user.is_authenticated:
        if User.query.filter_by(username = field.data).count():
            raise ValidationError('Username is already taken.')
  
class LoginForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2, max=20)])
    username = StringField("Username", [validators.Length(min=2, max=20), validate_first_username])
    password = PasswordField("Password")
    role = SelectField(u'Role', choices=[('admin', 'admin'), ('worker', 'worker')])
  
    class Meta:
        csrf = False

class UserForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2, max=20), validators.Optional()])
    username = StringField("Username", [validators.Length(min=2, max=20), validators.Optional()])
    password = PasswordField("Password")

    class Meta:
        csrf = False
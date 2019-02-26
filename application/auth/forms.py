from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField, validators
  
class LoginForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2, max=20)])
    username = StringField("Username", [validators.Length(min=2, max=20)])
    password = PasswordField("Password")
    role = SelectField(u'Role', choices=[('admin', 'admin'), ('worker', 'worker')])
  
    class Meta:
        csrf = False

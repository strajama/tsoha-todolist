from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    name = StringField("Name")
    username = StringField("Username", [validators.Length(min=2, max=144)])
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

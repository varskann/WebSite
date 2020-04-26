from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextField, TextAreaField
from wtforms.validators import DataRequired, Required, Email

csrf = CSRFProtect()

class ContactForm(FlaskForm):
  name = TextField("Name",  [Required()])
  email = TextField("Email",  [Required(), Email()])
  message = TextAreaField("Message",  [Required()])
  submit = SubmitField("Send")
from flask_wtf import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length

from backend.models.enums import AuthLevel


class UserProfileForm(FlaskForm):
    first_name = StringField('First Name:', render_kw={"disabled": "disabled"})
    last_name = StringField('Last Name:', render_kw={"disabled": "disabled"})
    email = StringField('Email:')
    username = StringField('Username:', render_kw={"disabled": "disabled"})
    password = PasswordField('Password:')
    auth_level = SelectField('Authorization level:', choices=["duck", "otter", "beaver"])
    submit = SubmitField('Update')

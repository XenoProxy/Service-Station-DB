from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
    DateField,
)
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class Clients(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    surname = StringField("Surname", validators=[DataRequired()])
    submit = SubmitField("Add")


class Auto(FlaskForm):
    vin = StringField("Vin", validators=[DataRequired()])
    number = StringField("Number", validators=[DataRequired()])
    brand = StringField("Brand", validators=[DataRequired()])
    model = StringField("Model", validators=[DataRequired()])
    make = DateField("Make", validators=[DataRequired()])
    submit = SubmitField("Add")

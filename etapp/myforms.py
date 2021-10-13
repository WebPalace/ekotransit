'''This module contains the class for all forms in my app, using flask to protect against csrf and for form validation since it is possible to disable JS validation'''

from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField
from wtforms.validators import DataRequired, Email


class Journey(FlaskForm):
    location= StringField(validators=[DataRequired()])
    destination= StringField(validators=[DataRequired()])
    submit= SubmitField("Submit")

# class Breakdown(FlaskForm):
#     location= StringField(validators=[DataRequired()])
#     destination= StringField(validators=[DataRequired()])
#     submit= SubmitField("Submit")

class Registration(FlaskForm):
    userfname= StringField("First Name: ",validators=[DataRequired()])
    userlname= StringField("Last Name: ",validators=[DataRequired()])
    email= StringField("Email: ",validators=[Email()])
    password= PasswordField("Password: ",validators=[DataRequired()])
    submit= SubmitField("Submit")

class UserLogin(FlaskForm):
    email= StringField("Email: ",validators=[Email()])
    password= PasswordField("Password: ",validators=[DataRequired()])
    submit= SubmitField("Submit")

class AdminLogin(FlaskForm):
    email= StringField("Email: ",validators=[Email()])
    password= PasswordField("Password: ",validators=[DataRequired()])
    submit= SubmitField("Submit")
    

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, RadioField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError, Regexp




class RegistrationForm(FlaskForm):
    firstname =  StringField('Firstname', validators=[DataRequired(), Length(min=5, max=30, message='should be atleast 5 characters long'),
                                                     Regexp('[a-zA-Z]+' ,message = 'name should contain only alphabats')])
    lastname =  StringField('Lastname', validators=[DataRequired(), Length(min=5, max=30, message='should be atleast 5 characters long')
                                                    , Regexp('[a-zA-Z]+' ,message = 'name should contain only alphabats')])
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=30, message='username should be atleast 5 characters long'),
                                                    Regexp('[a-zA-Z0-9]+' ,message = 'username should contain only alphabats and numbers')])
    email = StringField('Email Address', validators=[DataRequired(), Email(message='email  address should be valid')])
    gender = RadioField('Gender', choices=[('Female', 'Female'), ('Male', 'Male'), ('Others', 'Others')], validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=100, message='password should be atleast 8 characters long')])
    reenter_password = PasswordField('Reenter Password', validators=[EqualTo('password', message='reentered password should be similar to password')])
    submit = SubmitField('Create New Account')



class LoginForm(FlaskForm):
    email = StringField('Email Address', validators=[DataRequired(), Email(message='email  address should be valid')])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=100, message='password should be atleast 8 characters long')])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login Folk')
# -- Install package -- run in powershell
"""python -m pip install flask-wtf
   python -m pip install wtforms[email]"""

# import packages
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, SubmitField
from wtforms.validators import ValidationError, EqualTo, Email, DataRequired, Length

# Login page
class LoginForm(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired(), Length(min=2, max=20)]) # add more validation (check unique username)
    pwd = PasswordField('Password: ', validators=[DataRequired(), Length(min=8, max=20)]) # add more validation
    submit = SubmitField('Login')

# Forget Password page
class ForgetPwdForm(FlaskForm):
    email = StringField('Email: ', validators=[DataRequired(), Email('Invalid Email')])
    resetpwd = PasswordField('Reset Password: ', validators=[DataRequired(), Length(min=8, max=20)]) # add more validation
    submit = SubmitField('Reset Password')

# Register page
class RegisterForm(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired(), Length(min=2, max=20)]) # add more validation (check unique username)
    pwd = PasswordField('Password: ', validators=[DataRequired(), Length(min=8, max=20)]) # add more validation
    email = StringField('Email: ', validators=[DataRequired(), Email('Invalid Email')])
    gender = SelectField('Gender: ', choices=[('Male', 'Male'), ('Female', 'Female')])
    age = SelectField('Age Range: ', choices=[('Below 18', 'Below 18'), ('18-35', '18-35'), ('36-50', '36-50'), ('Above 50', 'Above 50')])
    jobnature = SelectField('Job Nature: ', choices=[('Business and Finance', 'Business and Finance'), ('Customer service', 'Customer service'), ('Education', 'Education'), ('Healthcare', 'Healthcare'), ('Hiring and Promotions', 'Hiring and Promotions'), ('Technology', 'Technology'), ('Others', 'Others')])
    jobranking = SelectField('Job Ranking: ', choices=[('Entry-level positions', 'Entry-level positions'), ('Middle management positions', 'Middle management positions'), ('Senior leadership positions', 'Senior leadership positions'), ('Others', 'Others')])
    ethnicity = SelectField('Ethnicity: ', choices=[('American Indian or Alaskan Native', 'American Indian or Alaskan Native'), ('Asian or Pacific Islander', 'Asian or Pacific Islander'), ('Black or African American', 'Black or African American'), ('Hispanic', 'Hispanic'), ('White or Caucasian', 'White or Caucasian'), ('Others', 'Others')])
    submit = SubmitField('Register')

# Your Profile (Edit Profile) page
# Account Info subpage
class ChangeAcctInfoForm(FlaskForm):
    email = StringField('Email: ', validators=[DataRequired(), Email('Invalid Email')])
    gender = SelectField('Gender: ', choices=[('Male', 'Male'), ('Female', 'Female')])
    age = SelectField('Age Range: ', choices=[('', 'Select an option'), ('Below 18', 'Below 18'), ('18-30', '18-30'), ('31-50', '31-50'), ('Above 50', 'Above 50')])
    jobnature = SelectField('Job Nature: ', choices=[('', 'Select an option'), ('Business and Finance', 'Business and Finance'), ('Customer service', 'Customer service'), ('Education', 'Education'), ('Healthcare', 'Healthcare'), ('Hiring and Promotions', 'Hiring and Promotions'), ('Technology', 'Technology'), ('Others', 'Others')])
    jobranking = SelectField('Job Ranking: ', choices=[('', 'Select an option'), ('Entry-level positions', 'Entry-level positions'), ('Middle management positions', 'Middle management positions'), ('Senior leadership positions', 'Senior leadership positions'), ('Others', 'Others')])
    ethnicity = SelectField('Ethnicity: ', choices=[('', 'Select an option'), ('American Indian or Alaskan Native', 'American Indian or Alaskan Native'), ('Asian or Pacific Islander', 'Asian or Pacific Islander'), ('Black or African American', 'Black or African American'), ('Hispanic', 'Hispanic'), ('White or Caucasian', 'White or Caucasian'), ('Others', 'Others')])
    save = SubmitField('Save changes')

# Your Profile (Edit Profile) page
# Change password subpage
class ChangeLoginInfoForm(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('New password: ', [DataRequired(), Length(min=8, max=20), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Repeat new password: ')
    change = SubmitField('Save changes')





# -- Install package -- run in powershell
"""python -m pip install flask-wtf
   python -m pip install wtforms[email]"""

# import packages
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, SubmitField
from wtforms.validators import ValidationError, EqualTo, Email, Length

# Login page
class LoginForm(FlaskForm):
    username = StringField(label=('Username:'), validators=[Length(min=2, max=20)]) 
    pwd = PasswordField(label=('Password:'), validators=[Length(min=6, max=20)])
    submit = SubmitField(label=('Login'))

# Forget Password page
class ForgetPwdForm(FlaskForm):
    email = StringField(label=('Email:'), validators=[Email('Invalid Email')])
    resetpwd = PasswordField(label=('Reset Password:'), validators=[Length(min=6, max=20)])
    submit = SubmitField(label=('Reset Password'))

# Register page
class RegisterForm(FlaskForm):
    username = StringField(label=('* Username:'), validators=[Length(min=2, max=20)])
    pwd = PasswordField(label=('* Password:'), validators=[Length(min=6, max=20)]) 
    email = StringField(label=('* Email:'), validators=[Email('Invalid Email')])
    gender = SelectField(label=('* Gender:'), choices=[('Male', 'Male'), ('Female', 'Female')])
    age = SelectField(label=('Age Range:'), choices=[('Below 18', 'Below 18'), ('18-35', '18-35'), ('36-50', '36-50'), ('Above 50', 'Above 50')])
    jobnature = SelectField(label=('Job Nature:'), choices=[('Business and Finance', 'Business and Finance'), ('Customer service', 'Customer service'), ('Education', 'Education'), ('Healthcare', 'Healthcare'), ('Hiring and Promotions', 'Hiring and Promotions'), ('Technology', 'Technology'), ('Others', 'Others')])
    jobranking = SelectField(label=('Job Ranking:'), choices=[('Entry-level positions', 'Entry-level positions'), ('Middle management positions', 'Middle management positions'), ('Senior leadership positions', 'Senior leadership positions'), ('Others', 'Others')])
    ethnicity = SelectField(label=('Ethnicity:'), choices=[('American Indian or Alaskan Native', 'American Indian or Alaskan Native'), ('Asian or Pacific Islander', 'Asian or Pacific Islander'), ('Black or African American', 'Black or African American'), ('Hispanic', 'Hispanic'), ('White or Caucasian', 'White or Caucasian'), ('Others', 'Others')])
    submit = SubmitField(label=('Register'))

# Your Profile (Edit Profile) page
# Account Info subpage
class ChangeAcctInfoForm(FlaskForm):
    email = StringField(label=('Email:'), validators=[Email('Invalid Email')])
    gender = SelectField(label=('Gender:'), choices=[('Male', 'Male'), ('Female', 'Female')])
    age = SelectField(label=('Age Range:'), choices=[('', 'Select an option'), ('Below 18', 'Below 18'), ('18-35', '18-35'), ('36-50', '36-50'), ('Above 50', 'Above 50')])
    jobnature = SelectField(label=('Job Nature:'), choices=[('', 'Select an option'), ('Business and Finance', 'Business and Finance'), ('Customer service', 'Customer service'), ('Education', 'Education'), ('Healthcare', 'Healthcare'), ('Hiring and Promotions', 'Hiring and Promotions'), ('Technology', 'Technology'), ('Others', 'Others')])
    jobranking = SelectField(label=('Job Ranking:'), choices=[('', 'Select an option'), ('Entry-level positions', 'Entry-level positions'), ('Middle management positions', 'Middle management positions'), ('Senior leadership positions', 'Senior leadership positions'), ('Others', 'Others')])
    ethnicity = SelectField(label=('Ethnicity:'), choices=[('', 'Select an option'), ('American Indian or Alaskan Native', 'American Indian or Alaskan Native'), ('Asian or Pacific Islander', 'Asian or Pacific Islander'), ('Black or African American', 'Black or African American'), ('Hispanic', 'Hispanic'), ('White or Caucasian', 'White or Caucasian'), ('Others', 'Others')])
    save = SubmitField(label=('Save changes'))

# Your Profile (Edit Profile) page
# Change password subpage
class ChangeLoginInfoForm(FlaskForm):
    new_username = StringField(label=('Username:'), validators=[Length(min=2, max=20)])
    new_pwd = PasswordField(label=('New password:'), validators=[Length(min=6, max=20), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField(label=('Repeat new password:'))
    change = SubmitField(label=('Save changes'))

class SentimentAnalysisForm(FlaskForm):
    ans = StringField('')
    submit = SubmitField(label=('Submit'))



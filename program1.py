#%%
"""! wget -O oracleinstantclient.zip https://download.oracle.com/otn_software/linux/instantclient/19600/instantclient-basic-linux.x64-19.6.0.0.0dbru.zip
! unzip -oq oracleinstantclient.zip
! mkdir -p /opt/oracle
! mv instantclient_19_6 /opt/oracle/
! sh -c "echo /opt/oracle/instantclient_19_6 > /etc/ld.so.conf.d/oracle-instantclient.conf"
! ln -s /usr/local/lib/python3.7/dist-packages/ideep4py/lib/libmkldnn.so.0 /usr/local/lib/python3.7/dist-packages/ideep4py/lib/libmkldnn.0.so
! ldconfig"""

# -- Install package -- run in powershell
"""
python -m pip install cx_Oracle
python -m pip install PySimpleGUI as sg
python -m pip install tabulatepython
python -m pip install Flask
python -m pip install flask-wtf
python -m pip install oracledb
python -m pip install flask-sqlalchemy"""

# Set up and connect to Oracle database
import oracledb

HOST_NAME = "IMZ409.ust.hk"
PORT_NUMBER = "1521"
SERVICE_NAME = "imz409"
USERNAME = "tykongaa"
PASSWORD = "1928"

conn = oracledb.connect(user=USERNAME, password=PASSWORD, port=PORT_NUMBER, host=HOST_NAME, service_name=SERVICE_NAME)

c = conn.cursor()

#%%
import sqlalchemy as sa
from flask import Flask, render_template, request, redirect, flash
from forms import LoginForm, ForgetPwdForm, RegisterForm, ChangeAcctInfoForm, ChangeLoginInfoForm
from sqlalchemy import Table, ForeignKey, Column, String
from sqlalchemy.ext.declarative import declarative_base

#Base = declarative_base()

# Declare variables and classes
login_username = ''

#class Member(Base):
    #pass
    #"""__table__ = Table('CS_MEMBER', Base.metadata,
                    #autoload=True, autoload_with=some_engine)"""

    
'''class Member:
    # init method or constructor
    def __init__(self, login_username, pwd, email, gender, age, job_nature, job_ranking, ethnicity):
        self.login_username = login_username
        self.pwd = pwd
        self.email = email
        self.gender = gender
        self.age = age
        self.job_nature = job_nature
        self.job_ranking = job_ranking
        self.ethnicity = ethnicity
    
    def retrieve(self):
        c.execute(
        """
        SELECT USERNAME, PWD, EMAIL, GENDER, AGE_RANGE, JOB_NATURE, JOB_RANKING, ETHNICITY
        FROM CS_MEMBER
        WHERE USERNAME = '{}'
        """.format(login_username)
        )

        for row in c:
            self.username = login_username
            self.pwd = row[1]
            self.email = row[2]
            self.gender = row[3]
            self.age = row[4]
            self.job_nature = row[5]
            self.job_ranking = row[6]
            self.ethnicity = row[7]'''



# initialization
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = '46fe7f11e7004b5beb341d9988e5b9b2'


# Flask API
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    login_form = LoginForm()
    login_msg = ''

    if request.method == 'POST':
        # Create variables
        username = request.form.get("username")  
        pwd = request.form.get("pwd")
        # SQL statement
        try:
            c.execute(
                """
                SELECT USERNAME, PWD
                FROM CS_MEMBER
                WHERE USERNAME = '{}'
                """.format(username)
            )
            for row in c:
                db_username = row[0]
                db_pwd = row[1]
            
            if username == db_username and pwd == db_pwd:
                global login_username
                login_username = db_username
                return redirect('/home')
        except:
            #flash("Incorrect username or password")
            pass
    else:
        pass
    
    return render_template('c_login.html', form=login_form)

@app.route('/forget', methods=['GET', 'POST'])
def forget_page():
    forget_form = ForgetPwdForm()

    if request.method == 'POST':
        # Create variables
        email = request.form.get("email")  
        resetpwd = request.form.get("resetpwd")
        # SQL statement
        c.execute(
            # check if input email exists
                """
                SELECT COUNT(*)
                FROM CS_MEMBER
                WHERE EMAIL = '{}'
                """.format(email)
            )
        for row in c:
            count = row[0]
        
        if count == 1:
            c.execute(
                """
                UPDATE CS_MEMBER
                SET PWD = '{}'
                WHERE EMAIL = '{}'
                """.format(resetpwd, email)
            )
            c.execute("commit")
            return redirect('/home')
        
    return render_template('c_forgetpwd.html', form=forget_form)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    register_form = RegisterForm()

    if request.method == 'POST':
        # Create variables
        username = request.form.get("username")  
        pwd = request.form.get("pwd")
        email = request.form.get("email")  
        gender = request.form.get("gender")
        age = request.form.get("age")
        job_nature = request.form.get("job-nature")
        job_ranking = request.form.get("job-ranking")
        ethnicity = request.form.get("ethnicity")

        # SQL statement
        c.execute(
                """
                INSERT INTO CS_MEMBER (USERNAME, PWD, EMAIL, GENDER, AGE_RANGE, JOB_NATURE, JOB_RANKING, ETHNICITY)
                VALUES ('{}', '{}', '{}', '{}', '{}','{}', '{}', '{}')
                """.format(username, pwd, email, gender, age, job_nature, job_ranking, ethnicity)
            )
        c.execute("commit")
        # flash('Thanks for registering')
        return redirect('/home')
    return render_template('c_register.html', form=register_form)
    
    """# Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.register_form['username']
        password = request.register_form['password']
        email = request.register_form['email']
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('c_register.html', form=register_form, msg=msg)"""

@app.route('/home', methods=['GET', 'POST'])
def home_page():
    return render_template('c_main.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile_page():
    acctinfo_form = ChangeAcctInfoForm()
    logininfo_form = ChangeLoginInfoForm()

    # acctinfo_form
    if "ChangeAcctInfoForm" in request.form and request.method == 'POST':
        # Create variables
        email = request.form.get("email")
        gender = request.form.get("gender")
        age = request.form.get("age")
        job_nature = request.form.get("job-nature")
        job_ranking = request.form.get("job-ranking")
        ethnicity = request.form.get("ethnicity")

        # SQL statement
        c.execute(
                """
                UPDATE CS_MEMBER 
                SET EMAIL = '{}',
                GENDER = '{}',
                AGE_RANGE = '{}', 
                JOB_NATURE = '{}', 
                JOB_RANKING = '{}', 
                ETHNICITY = '{}'
                WHERE USERNAME = '{}'
                """.format(email, gender, age, job_nature, job_ranking, ethnicity, login_username)
            )
        c.execute("commit")
        #flash()

    # logininfo_form
    if "ChangeLoginInfoForm" in request.form and request.method == 'POST':
        new_username = request.form.get("username")
        new_pwd = request.form.get("pwd")

        # SQL statement
        c.execute(
                """
                UPDATE CS_MEMBER 
                SET USERNAME = '{}',
                PWD = '{}'
                WHERE USERNAME = '{}'
                """.format(new_username, new_pwd, login_username)
            )
        c.execute("commit")
        #flash()

    return render_template('c_profile.html', acctinfo_form=acctinfo_form, logininfo_form=logininfo_form)

@app.route('/toolkit', methods=['GET', 'POST'])
def view_page():
    return render_template('c_view.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz_page():
    return render_template('c_quiz_start.html')

@app.route("/quiz-question", methods=['GET', 'POST'])
def quiz_question():
    return render_template('c_quiz_question.html')

if __name__=="__main__":
    app.run(debug=True)
#! export FLASK_APP=program.py
#! flask --app program run"""



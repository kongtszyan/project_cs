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
python -m pip install PySimpleGUI as sg
python -m pip install tabulatepython
python -m pip install Flask
python -m pip install flask-wtf
python -m pip install oracledb
python -m pip install flask-sqlalchemy
python -m pip install pysentiment2"""

# Set up and connect to Oracle database
import oracledb

HOST_NAME = "IMZ409.ust.hk"
PORT_NUMBER = "1521"
SERVICE_NAME = "imz409"
USERNAME = "tykongaa"
PASSWORD = "1928"

conn = oracledb.connect(user=USERNAME, password=PASSWORD, port=PORT_NUMBER, host=HOST_NAME, service_name=SERVICE_NAME)

c = conn.cursor()

# Import packages
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, flash
from forms import LoginForm, ForgetPwdForm, RegisterForm, ChangeAcctInfoForm, ChangeLoginInfoForm, SentimentAnalysisForm
from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey
from sqlalchemy.ext.automap import automap_base


# Initialization
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = '46fe7f11e7004b5beb341d9988e5b9b2'
#app.config['SQLALCHEMY_DATABASE_URI']='oracle+oracledb://tykongaa:1928@IMZ409.ust.hk:1521/?service_name=imz409'
#engine = create_engine('oracle+oracledb://tykongaa:1928@IMZ409.ust.hk:1521/?service_name=imz409')
#db = SQLAlchemy(app)

#Base = automap_base()
#Base.prepare(db.engine, reflect=True)
#Member, Bias = Base.classes.cs_member, Base.classes.cs_bias
#members = db.session.query(Member).all()
#for i in members:
#    print(i.username)

# Declare variables and classes
login_username = ''

'''class CS_Member(Base):

    # init method or constructor
    def __init__(self, login_username, pwd, email, gender, age, job_nature, job_ranking, ethnicity):
        id = sa.Column(sa.Integer, primary_key=True)
        name = sa.Column(sa.String)
        email = sa.Column(sa.String)
        self.gender = gender
        self.age = age
        self.job_nature = job_nature
        self.job_ranking = job_ranking
        self.ethnicity = ethnicity
    
    def retrieve(self, login_username):
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
            self.ethnicity = row[7]
        print(Member.username)
        print(Member.pwd)'''

class Member:
    # init method or constructor
    def __init__(self):
        self.username = None
        self.pwd = None
        self.email = None
        self.gender = None
        self.age = None
        self.job_nature = None
        self.job_ranking = None
        self.ethnicity = None
    
    '''@classmethod
    def from_row(cls, row):
        for row in c:
            mem.username = login_username
            mem.pwd = row[1]
            mem.email = row[2]
            mem.gender = row[3]
            mem.age = row[4]
            mem.job_nature = row[5]
            mem.job_ranking = row[6]
            mem.ethnicity = row[7]
            print(mem.username)
            print(mem.pwd)

    @classmethod
    def retrieve_by_username(cls, login_username):
        c.execute(
        """
        SELECT USERNAME, PWD, EMAIL, GENDER, AGE_RANGE, JOB_NATURE, JOB_RANKING, ETHNICITY
        FROM CS_MEMBER
        WHERE USERNAME = '{}'
        """.format(login_username)
        )
        row = c.fetchone()
        mem = cls.from_row(row)

        return mem'''

    
# Flask API
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    global login_username
    login_username = None
    login_form = LoginForm(request.form)
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
    forget_form = ForgetPwdForm(request.form)

    if request.method == 'POST' and forget_form.validate():
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
    register_form = RegisterForm(request.form)

    if request.method == 'POST' and register_form.validate():
        # Create variables
        username = request.form.get("username")  
        pwd = request.form.get("pwd")
        email = request.form.get("email")  
        gender = request.form.get("gender")
        age = request.form.get("age")
        job_nature = request.form.get("job-nature")
        job_ranking = request.form.get("job-ranking")
        ethnicity = request.form.get("ethnicity")

        #try:
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
        #except:
            #pass
            #flash('')
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
    acctinfo_form = ChangeAcctInfoForm(request.form)
    logininfo_form = ChangeLoginInfoForm(request.form)

    # Retrieve as default values
    c.execute(
    """
    SELECT USERNAME, PWD, EMAIL, GENDER, AGE_RANGE, JOB_NATURE, JOB_RANKING, ETHNICITY
    FROM CS_MEMBER
    WHERE USERNAME = '{}'
    """.format(login_username)
    )
    rows = c.fetchall()

    # acctinfo_form
    if "ChangeAcctInfoForm" in request.form and request.method == 'POST' and acctinfo_form.validate():
        # Create variables
        email = request.form.get("email")
        gender = request.form.get("gender")
        age = request.form.get("age")
        job_nature = request.form.get("job-nature")
        job_ranking = request.form.get("job-ranking")
        ethnicity = request.form.get("ethnicity")

        # SQL statement to update values
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
    if "ChangeLoginInfoForm" in request.form and request.method == 'POST' and logininfo_form.validate():
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

    return render_template('c_profile.html', acctinfo_form=acctinfo_form, logininfo_form=logininfo_form, rows=rows)

@app.route('/toolkit', methods=['GET', 'POST'])
def view_page():
    # count number of rows in database
    c.execute(
    """
    SELECT BIAS_ID, TITLE
    FROM CS_BIAS
    """
    )
    bid_list = []
    btitle_list = []
    for row in c:
        bid_list.append(row[0])
        btitle_list.append(row[1])

    title = request.args.get('title')
    # Set the value of the Python variable
    my_variable = title

    c.execute(
    """
    SELECT NAME, SUBTITLE, b.DESCRIPTION, t.DESCRIPTION, EXAMPLE
    FROM CS_BIAS b INNER JOIN CS_TOOLKIT t
    ON b.BIAS_ID = t.BIAS_ID
    WHERE b.BIAS_ID = '{}'
    """.format(2)
    )
    for info in c:
        name = info[0]
        #image = info[1]
        subtitle = info[1]
        description = info[2]
        toolkit = info[3]
        example = info[4]
#name=name, image=image, subtitle=subtitle, description=description, toolkit=toolkit, example=example
    return render_template('c_view.html', name=name, subtitle=subtitle, description=description, toolkit=toolkit, example=example)

@app.route('/quiz', methods=['GET', 'POST'])
def quiz_page():
    return render_template('c_quiz_start.html')

@app.route("/quiz-question", methods=['GET', 'POST'])
def quiz_question():
    # question
    questions = []
    questions.clear()
    c.execute(
    """
    SELECT QUESTION_TEXT
    FROM CS_QUESTION
    """
    )
    for row in c:
        questions.append(row)

    return render_template('c_quiz_question.html', questions=questions)

@app.route("/quiz-result", methods=['GET', 'POST'])
def quiz_result():
    # answer
    sa_form = SentimentAnalysisForm()
    responses = []
    responses.clear()
    if request.method == 'POST':
        ans = request.form.get("sa")
        responses.append(ans)
    
    #import sys
    #print("a", file=sys.stdout)
    
    return render_template('c_quiz_result.html', form=sa_form, responses=responses)

if __name__=="__main__":
    app.run(debug=True)
#! export FLASK_APP=program.py
#! flask --app program run"""

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
python -m pip install Flask"""

# Set up and connect to Oracle database
#python -m pip install oracledb
import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir= r"C:\Users\kongt\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts\instantclient_21_10")

HOST_NAME = "IMZ409.ust.hk"
PORT_NUMBER = "1521"
SERVICE_NAME = "imz409"
USERNAME = "tykongaa"
PASSWORD = "1928"

dsn_tns = cx_Oracle.makedsn(HOST_NAME, PORT_NUMBER, service_name=SERVICE_NAME) 
conn = cx_Oracle.connect(user=USERNAME, password=PASSWORD, dsn=dsn_tns)

c = conn.cursor()

#%%
from flask import Flask, render_template
app = Flask(__name__, template_folder='templates',
            static_folder='static')

@app.route('/home')
def home_page():
    return render_template('c_main.html')

@app.route('/profile')
def profile_page():
    return render_template('c_profile.html')

@app.route('/toolkit')
def view_page():
    return render_template('c_view.html')

@app.route('/quiz')
def quiz_page():
    return render_template('c_quiz_start.html')

@app.route("/quiz-question")
def quiz_question():
    return render_template('c_quiz_question.html')

if __name__=="__main__":
    app.run(debug=True)
#! export FLASK_APP=program.py
#! flask --app program run"""
# %%

# SQL testing
c.execute("""
SELECT * FROM STUDENT
WHERE S_ID = '21'
"""
)
for row in c:
    print(row[0])
# %%

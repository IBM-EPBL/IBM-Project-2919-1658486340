import errno
import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, url_for, render_template, request, redirect, session
from flask_session import Session
import utils
from datetime import datetime


app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')
app.config['SESSION_TYPE'] = 'filesystem'
PERMANENT_SESSION_LIFETIME = 1800
app.config['SECRET_KEY'] = 'bd8307d3767b4c67b1b3086a657c2ef4'
app.config.update(SECRET_KEY=os.random(24))
db = SQLAlchemy(app)
app.config.from_object(__name__)

Session(app)

PERMANENT_SESSION_LIFETIME = 1800


def check_credentials(e, p):
    if utils.getPassword(e) == p:
        session['logged_in'] = True
        session['email'] = e
        print("Valid User")
        return redirect(url_for('dashboard'))
    return render_template('login.html', error="Invalid Credentials")


def register(u, p, e):
    print(u, p, e)
    try:
        r = utils.addUser(u, e, p)
        if (r == "Username Exists"):
            return render_template('signup.html', error="Username Exists")
        return render_template('login.html')
    except:
        return render_template('signup.html', error="Error in inserting user")


def add_finance_record(e, a, c, d, dt):
    try:
        r = utils.createFinanceRecord(e, a, c, d, dt)
        return redirect(url_for('dashboard'))
    except:
        return redirect(url_for('dashboard'))


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print("Checking Credentials")
        return check_credentials(request.form['email'], request.form['password'])
    else:
        if session.get('logged_in'):
            return redirect(url_for('dashboard'))
        return render_template('login.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        email = session['email']
        now = datetime.now()
        dt_string = now.strftime("%Y/%m/%d %H:%M")
        date = dt_string
        print(date)
        return add_finance_record(email, request.form['category'], request.form['amount'], request.form['description'], date)
    else:
        if session.get('logged_in'):
            email = session['email']
            rows = utils.fetchFinanceRecord(email)
            l = len(rows)
            return render_template('dashboard.html', rows=rows, len=l)
        return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        return register(request.form['name'], request.form['password'], request.form['email'])
    else:
        return render_template('signup.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
    # app.run(host="0.0.0.0", port=5000)

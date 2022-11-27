from flask import Flask, render_template, request, redirect, url_for, session
import requests
import flash
import ibm_db
from flask_login import UserMixin
from ibm_db import exec_immediate
from flask_session import Session
import re
import connect
import utils

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abf6703a27964e61953307e963426a04'

dbname = "bludb"
username = "txs49042"
password = "cNEKMzATxRu70nLU"
hostname = "125f9f61-9715-46f9-9399-c8177b21803b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud"
cert = "DigiCertGlobalRootCA.crt"
port = 30426
protocol = "TCPIP"
conn = connect.conn


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login(name, password):
    if request.method == 'POST':
        print("Checking Credentials")
        return check_credentials(request.form['email'], request.form['password'])
    else:
        if session.get('logged_in'):
            return redirect(url_for('dashboard'))
        return render_template('login.html')


@app.route('/signup', methods=["GET", "POST"])
def Signup():
    if request.method == 'POST':
        arr = []
        try:
            name = request.form['name']
            password = request.form['password']
            phone = request.form['phone']
            email = request.form['email']
            sql = "insert into registration(name, email, password, phone) values (?, ?, ?, ?), (name, email, password, phone)"
            stmt = ibm_db.exec_immediate(conn, sql)
            conn.fetch_assoc(stmt)
            flash("Record added successfully", "success")
        except:
            flash("Error in insert", "danger")
        finally:
            return redirect(url_for("dashboard"))
            conn.close()
    return render_template("signup.html")


def check_credentials(e, p):
    if utils.getPassword(e) == p:
        session['logged_in'] = True
        session['email'] = e
        print("Valid User")
        return redirect(url_for('dashboard'))
    return render_template('login.html', error="Invalid Credentials")


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route('/graph')
def graph():
    return render_template("graph.html")


@app.route('/transactionList')
def transactionList():
    return render_template("transactionList.html")


@app.route('/addTransactionList')
def addTransactionList():
    return render_template("addTransaction.html")


@app.route('/logout')
def logout():
    session.clear()
    session['logged_in'] = False
    return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

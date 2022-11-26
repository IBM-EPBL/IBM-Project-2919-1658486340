from flask import Flask, render_template, request, redirect, url_for, session
import requests
import flash
import ibm_db
from flask_login import UserMixin
from ibm_db import exec_immediate
from flask_session import Session
import re
import connect


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
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        sql = "SELECT * FROM registration WHERE name=? AND password=?, (name, password)"
        stmt = ibm_db.exec_immediate(conn, sql)
        res = conn.fetch_assoc(stmt)
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
    return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

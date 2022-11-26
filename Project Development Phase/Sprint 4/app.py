from flask import Flask, render_template, request, redirect, url_for, session
import requests
import flash
import ibm_db
from ibm_db import exec_immediate
from flask_session import Session
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

conn = ibm_db.connect(
    f"DATABASE={dbname};HOSTNAME={hostname};PORT={port};PROTOCOL={protocol};UID={username};PWD={password};SECURITY=SSL;SSLServerCertificate={cert};", "", "")


def Connection():
    try:
        conn = ibm_db.connect(
            f"DATABASE={dbname};HOSTNAME={hostname};PORT={port};PROTOCOL={protocol};UID={username};PWD={password};SECURITY=SSL;SSLServerCertificate={cert};", "", "")
        print("Database Connected Successfully !")
        conn.execute(
            "create table if not exists txs49042.users(id integer primary key, name text, password password, contact text, email text )")
        return conn
    except:
        print("Unable to connect: ", ibm_db.conn_errormsg())


Connection()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        sql = "SELECT * FROM txs49042.users WHERE name=? AND password=?, (name, password)"
        stmt = ibm_db.exec_immediate(conn, sql)
        res = conn.fetch_assoc(stmt)
        data = res.fetchone()
    if data:
        session["name"] = data["name"]
        session["password"] = data["password"]
        return redirect("dashboard")
    else:
        flash("Username and password doesn't match", "danger")
    return render_template('login.html')


@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        arr = []
        try:
            name = request.form['name']
            password = request.form['password']
            phone = request.form['phone']
            email = request.form['email']
            conn = Connection()
            sql = "insert into txs49042.USER(name, phone, email, password) values (?, ?, ?, ?), (name, phone, email, password)"
            stmt = ibm_db.exec_immediate(conn, sql)
            conn.row_factory = conn.fetch_assoc(stmt)
            flash("Record added successfully", "success")
        except:
            flash("Error in insert", "danger")
        finally:
            return redirect(url_for("dashboard"))
            conn.close()
    return render_template("signup.html")


def check_credentials(e, p):
    if utils.getPassword(e) == p:
        Session['logged_in'] = True
        Session['email'] = e
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
    return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

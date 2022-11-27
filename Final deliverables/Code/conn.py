import ibm_db
from ibm_db import tables
from ibm_db import fetch_assoc
from ibm_db import exec_immediate

dbname = "bludb"
username = "txs49042"
password = "cNEKMzATxRu70nLU"
hostname = "125f9f61-9715-46f9-9399-c8177b21803b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud"
cert = "DigiCertGlobalRootCA.crt"
port = 30426
protocol = "TCPIP"

db = ibm_db

def establish():
    try:
        conn = db.connect(
            f"DATABASE={dbname};HOSTNAME={hostname};PORT={port};PROTOCOL={protocol};UID={username};PWD={password}; SECURITY=SSL; SSLServerCertificate={cert};",
            "", "")
        print("Connected to database")
        return conn
    except:
        print("Error connecting to database")



def insertuser(conn1, name, email, user, passw):
    sql = "INSERT INTO users(name,email,username,password) VALUES ('{}','{}','{}','{}')".format(
        name, email, user, passw)
    try:
        stmt = db.exec_immediate(conn1, sql)
        print("Number of affected rows: ", db.num_rows(stmt))
    except:
        print("cannot insert user to database")

def useremail_check(conn, email):
    sql = "SELECT * FROM users WHERE email='{}' ".format(email)
    stmt = db.exec_immediate(conn, sql)
    results = db.fetch_assoc(stmt)
    if results == False:
        return True
    else:
        return False


def user_check(conn, email, passw):
    sql = "SELECT * FROM users WHERE email='{}' AND password='{}'".format(
        email, passw)
    stmt = db.exec_immediate(conn, sql)
    results = db.fetch_both(stmt)
    return results


def setuser(conn, money, budget, goal, email, pwd):
    sql = "UPDATE USERS SET(pocketmoney,budget,monthlygoal) = ('{}','{}','{}') WHERE email='{}' AND password='{}'".format(
        money, budget, goal, email, pwd)
    try:
        stmt = db.exec_immediate(conn, sql)
        print("Number of affected rows: ", db.num_rows(stmt))
    except:
        print("Error inserting data to database")


def inserttransac(conn, id, amt, des, cat):
    sql = "INSERT INTO TRANSACTIONS(user_id,amount,description,category) VALUES('{}','{}','{}','{}')".format(
        id, amt, des, cat)
    try:
        stmt = db.exec_immediate(conn, sql)
        print("Number of affected rows: ", db.num_rows(stmt))
    except:
        print("Error inserting data to database")



def gettotalsum(conn, id):
    sql = "SELECT SUM(amount) as SUM FROM transactions WHERE MONTH(date) = MONTH(CURRENT DATE) AND YEAR(date) = YEAR(CURRENT DATE) AND user_id='{}'".format(id)
    try:
        stmt = db.exec_immediate(conn, sql)
        res = db.fetch_both(stmt)
        return res
    except:
        print("Error while fetching")



def getalltransac(conn, id):
    sql = "SELECT * FROM transactions WHERE MONTH(date) = MONTH(CURRENT DATE) AND YEAR(date) = YEAR(CURRENT DATE) AND user_id='{}' ORDER BY date DESC".format(id)
    try:
        stmt = db.exec_immediate(conn, sql)
        res = db.fetch_both(stmt)
        if (res == False):
            return []
        else:
            res['DATE'] = res['DATE'].date()
            dict = [{'id': res['ID'], 'date': res['DATE'], 'amt': res['AMOUNT'],
                     'cat': res['CATEGORY'], 'des':res['DESCRIPTION']}]
            res = db.fetch_both(stmt)
            while (res != False):
                res['DATE'] = res['DATE'].date()
                dict.append({'id': res['ID'], 'date': res['DATE'], 'amt': res['AMOUNT'],
                            'cat': res['CATEGORY'], 'des': res['DESCRIPTION']})
                res = db.fetch_both(stmt)
            return dict
    except:
        print("Error while fetching")


def deletetrans(conn, id):
    sql = "DELETE FROM transactions WHERE id='{}'".format(id)
    try:
        stmt = db.exec_immediate(conn, sql)
        print("Number of affected rows: ", db.num_rows(stmt))
    except:
        print("Error deleting data from database")

def updateTrans(conn, id, amt, des):
    sql = "UPDATE transactions SET AMOUNT='{}',DESCRIPTION = '{}' WHERE ID='{}'".format(
        amt, des, id)
    try:
        stmt = db.exec_immediate(conn, sql)
        print("Number of affected rows: ", db.num_rows(stmt))
    except:
        print("Successfully updated transaction")


def get_budget(conn, id):
    sql = "SELECT POCKETMONEY FROM users WHERE ID='{}' ".format(id)
    stmt = db.exec_immediate(conn, sql)
    results = db.fetch_assoc(stmt)
    return results
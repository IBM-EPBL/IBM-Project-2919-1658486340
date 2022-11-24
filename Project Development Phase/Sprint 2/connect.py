import ibm_db

dbname = "bludb"
username = "txs49042"
password = "cNEKMzATxRu70nLU"
hostname = "125f9f61-9715-46f9-9399-c8177b21803b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud"
cert = "DigiCertGlobalRootCA.crt"
port = 30426
protocol = "TCPIP"

conn = ibm_db.connect(
"DATABASE={dbname};HOSTNAME={hostname};PORT={port};PROTOCOL={protocol};UID={username};PWD={password};SECURITY=SSL;SSLServerCertificate={cert};", "", "")
# conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=125f9f61-9715-46f9-9399-c8177b21803b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud:30426;PORT=30426;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=txs49042;PWD=cNEKMzATxRu70nLU", "", "")


def executingDB(cmd):
    return (conn, cmd)


def executingReturn(cmd):
    return (conn, cmd)


# Sql performances

def addUser(username, email, password):
    sql_fd = f"SELECT * FROM user WHERE username='{username}'"
    r = executingReturn(sql_fd)

    if r != []:
        return "Username Exists"

    sql_st = f"INSERT INTO user(username , email , pass ) values ( '{username}' , '{email}' , '{password}' )"
    u = executingDB(sql_st)
    return "User registered successfully"


def getPassword(username):
    sql_fd = f"SELECT pass FROM user WHERE username='{username}'"
    r = executingReturn(sql_fd)
    u = executingDB(sql_fd)
    print("SURNAME "+u+"PASS"+r)
    return r[0]['PASS']


def fetchFinanceRecord(username):
    sql_fd = f"SELECT * FROM finance WHERE username='{username}'"
    r = executingReturn(sql_fd)
    return r


def createFinanceRecord(username, amount, category, description, date):
    sql_st = f"INSERT INTO finance(username , amount , category , description , date ) values ( '{username}' , '{amount}' , '{category}' , '{description}' , '{date}' )"
    r = executingDB(sql_st)
    return "Record created successfully"

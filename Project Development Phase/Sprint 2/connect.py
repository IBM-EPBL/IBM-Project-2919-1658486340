import ibm_db
from ibm_db import tables
from ibm_db import fetch_assoc
from ibm_db import exec_immediate

dbname = ""
username = ""
password = ""
hostname = "0"
crt = ""
port = ""
protocol = "TCPIP"
t = 1


def results(command):
    ret = []
    result = fetch_assoc(command)

    while result:
        ret.append(result)
        result = fetch_assoc(command)
    return ret


conn = ibm_db.connect(
    f"DATABASE={dbname};"
    f"HOSTNAME={hostname};"
    f"PORT={port};PROTOCOL={protocol};"
    f"UID={username};PWD={password};"
    f"SECURITY=SSL;"
    f"SSLServerCertificate={crt};",
    "", "")


def execDB(cmd):
    return exec_immediate(conn, cmd)


def execReturn(cmd):
    return results(exec_immediate(conn, cmd))

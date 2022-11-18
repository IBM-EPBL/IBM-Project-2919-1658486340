import ibm_db
from ibm_db import tables
from ibm_db import fetch_assoc
from ibm_db import exec_immediate

#  For security purposes this sec havent added
dbname = ""
username = ""
password = ""
hostname = ""
cert = ""
port = 31198
protocol = "TCPIP"


def results(command):
    ret = []
    result = fetch_assoc(command)

    while result:
        ret.append(result)
        result = fetch_assoc(command)
    return ret


conn = ibm_db.pconnect(
    f"DATABASE={dbname};HOSTNAME={hostname};PORT={port};PROTOCOL={protocol};UID={username};PWD={password};SECURITY=SSL;SSLServerCertificate={cert};", "", "")


def execDB(cmd):
    return exec_immediate(conn, cmd)


def execReturn(cmd):
    return results(exec_immediate(conn, cmd))

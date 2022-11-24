import ibm_db


#  For security purposes this sec havent added
dbname = "bludb"
username = "txs49042"
password = "cNEKMzATxRu70nLU"
hostname = "125f9f61-9715-46f9-9399-c8177b21803b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud"
cert = "DigiCertGlobalRootCA.crt"
port = 30426
protocol = "TCPIP"




conn = ibm_db.connect(
    f"DATABASE={dbname};HOSTNAME={hostname};PORT={port};PROTOCOL={protocol};UID={username};PWD={password};SECURITY=SSL;SSLServerCertificate={cert};", "", "")
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=125f9f61-9715-46f9-9399-c8177b21803b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud:30426;PORT=30426;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=txs49042;PWD=cNEKMzATxRu70nLU", "", "")


def execDB(cmd):
    return exec_immediate(conn, cmd)


def execReturn(cmd):
    return results(exec_immediate(conn, cmd))

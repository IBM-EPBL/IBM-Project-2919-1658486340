from connect import executingDB, executingReturn


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
    print("SURNAME "+"PASS"+r)
    return r[0]['PASS']


def fetchFinanceRecord(username):
    sql_fd = f"SELECT * FROM finance WHERE username='{username}'"
    r = executingReturn(sql_fd)
    return r


def createFinanceRecord(username, amount, category, description, date):
    sql_st = f"INSERT INTO finance(username , amount , category , description , date ) values ( '{username}' , '{amount}' , '{category}' , '{description}' , '{date}' )"
    r = executingDB(sql_st)
    return "Record created successfully"

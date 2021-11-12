import mysql.connector

def selectAccount():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="@2027",
        database="ftpclient"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM account")

    myresult = mycursor.fetchone()
    return myresult
    # print(myresult[1])

def updateAccount(host, user, passwd, port):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="@2027",
            database="ftpclient"
        )

        mycursor = mydb.cursor()
        print("Hello")
        sql = "UPDATE account SET host = %s, username = %s, password = %s, port = %s WHERE id = '1'"
        data = (host, user, passwd, port)
        print("Hello")
        mycursor.execute(sql, data)
        print("Hello")
        mydb.commit()
        return True
    except ValueError:
        print(ValueError)
        return False
    # print(mycursor.rowcount, "record(s) affected")
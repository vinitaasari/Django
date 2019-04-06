import mysql.connector as mysql

def getConnection():
    db = mysql.connect(host="localhost",user="root",password="",database="pythondb")
    cr=db.cursor()
    return db

def executequery(query):
    con=getConnection()
    cr=con.cursor()
    cr.execute(query)
    con.commit()
    
import mysql.connector
d={
    "user":"root",
    "password":"",
    "host":"localhost"
}
con=mysql.connector.connect(**d)
cursor=con.cursor()
s='''CREATE DATABASE testcurd'''
cursor.execute(s)
con.close
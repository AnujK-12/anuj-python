import mysql.connector
d={
    "user":"root",
    "password":"",
    "host":"localhost",
    "database":"testcurd"
}
con=mysql.connector.connect(**d)
cursor=con.cursor()
s='''DELETE FROM employee where id=3'''

cursor.execute(s)
con.commit()
con.close()
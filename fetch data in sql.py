import mysql.connector
d={
    "user":"root",
    "password":"",
    "host":"localhost",
    "database":"testcurd"
}
con=mysql.connector.connect(**d)
cursor=con.cursor()
s='''select * from employee'''
cursor.execute(s)
# print(cursor.fetchall())
# print(cursor.fetchmany(3))
print(cursor.fetchone())
con.close()


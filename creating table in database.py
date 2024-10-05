import mysql.connector
d={
    "user":"root",
    "password":"",
    "host":"localhost",
    "database":"testcurd"
}
con=mysql.connector.connect(**d)
cursor=con.cursor()

s='''
CREATE TABLE employee(
id int PRIMARY KEY AUTO_INCREMENT,
name varchar(20),
gender char(1),
department varchar(20)
)'''
cursor.execute(s)
con.close()

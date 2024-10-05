import mysql.connector
d={
    "user":"root",
    "password":"",
    "host":"localhost",
    "database":"testcurd"
}
con=mysql.connector.connect(**d)
cursor=con.cursor()
# s='''UPDATE employee SET name="Harsh" WHERE id=1'''
id=input("Enter the ID to be updated")   # updating through user
name=input("Enter a new name :")
gen=input("Enter the gender :")
dep=input("Enter a nuw department")
s='''UPDATE employee SET name=%s,gender=%s,department=%s WHERE id=%s'''
cursor.execute(s,(name,gen,dep,id))
con.commit()
con.close()
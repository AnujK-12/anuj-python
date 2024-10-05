import mysql.connector
d={
    "user":"root",
    "password":"",
    "host":"localhost",
    "database":"testcurd"
}
con=mysql.connector.connect(**d)
cursor=con.cursor()
# name= input("Enter name ")
# gender=input("Enter gender")
# dep=input("enter department name ")  # entering values by user

# s='''INSERT INTO EMPLOYEE(name,gender,department) VALUES(%s,%s,%s)'''
# data=[("John","M","Marketing"),("Oscar","M","Finance"),("Holly","F","HR")] # entering multiple values using list
s='''insert into employee values(3,"Sujal","M","Finance")'''
cursor.execute(s)
con.commit()
con.close()

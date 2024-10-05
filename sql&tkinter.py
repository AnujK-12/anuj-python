from tkinter import *
from country_list import b
import re
import mysql.connector
d={
    "user":"root",
    "password":"",
    "host":"localhost",
    "database":"testcurd"
}
con=mysql.connector.connect(**d)
cursor=con.cursor()
id_update=0

def create_table():
    
    s='''
    CREATE TABLE IF NOT EXISTS studentinfo(
    id int PRIMARY KEY AUTO_INCREMENT,
    name varchar(20),
    gender char(1),
    email_id varchar(20),
    country varchar(20),
    language varchar(20)
    )'''
    cursor.execute(s)

def show_data_in_control(id):
    global gender
    global id_update
    id_update=id
    s='''Select * from studentinfo where id=%s'''
    cursor.execute(s,(id,))
    data=cursor.fetchone()
    nameEntry.delete(0,END)
    nameEntry.insert(0,data[1])
    emailEntry.delete(0,END)
    emailEntry.insert(0,data[3])
    if(data[2]=="M"):
        gender.set(1)
    elif(data[2]=="F"):
        gender.set(2)
    print(data)
    cpp.set(0)
    python.set(0)
    java.set(0)
    lang=re.split(",",data[5])
    if("C++" in lang):
        cpp.set(1)
    if("Python" in lang):
        python.set(1)
    if("Java" in lang):
        java.set(1)
    print(lang)
    l
    p=l.get(0,END).index(data[4])
    l.selection_clear(0,END)
    l.selection_set(p,p)
    l.yview_scroll(p,"units")

def show_data():
    s='''SELECT * from studentinfo'''
    cursor.execute(s)
    data=cursor.fetchall()
    r=7
    for i in data:
        iLabel=Label(top,text=i[0])
        nLabel=Label(top,text=i[1])
        eLabel=Label(top,text=i[2])
        gLabel=Label(top,text=i[3])
        lLabel=Label(top,text=i[4])
        cLabel=Label(top,text=i[5])
        updateButton=Button(top,text="Show Profile",command=lambda id=i[0]: show_data_in_control(id))
        deleteButton=Button(top,text="Delete Profile",command=lambda id=i[0]: delete_data(id))
        iLabel.grid(row=r,column=0)
        nLabel.grid(row=r,column=1)
        eLabel.grid(row=r,column=2)
        gLabel.grid(row=r,column=3)
        lLabel.grid(row=r,column=4)
        cLabel.grid(row=r,column=5)
        updateButton.grid(row=r,column=6)
        deleteButton.grid(row=r,column=7)
        r +=1

def datas():
    name=nameEntry.get()
    email=emailEntry.get()
    if(gender.get()==1):
        g="M"
    elif(gender.get()==2):
        g="F"
    language =""
    if (cpp.get()==1):
        language +="C++,"
    if(python.get()==1):
        language +="Python,"
    if(java.get()==1):
        language+="Java"
    country=l.get(l.curselection())
    return(name,email,g,language,country)


def store_data():
    name,email,g,language,country=datas()

    s='''INSERT into studentinfo (name,email_id,gender,language,country) values(%s,%s,%s,%s,%s)'''
    cursor.execute(s,(name,email,g,language,country))
    con.commit()

def update_data():
    global id_update
    s='''update studentinfo set name=%s,email_id=%s,gender=%s,language=%s,country=%s where id=%s '''
    name,email,g,language,country=datas()
    cursor.execute(s,(name,email,g,language,country,id_update))
    con.commit()

def delete_data(id):
    
    s='''delete from studentinfo where id=%s'''
    cursor.execute(s,(id,))
    con.commit()


top=Tk()
top.geometry("800x500")

# Creating Menu
menubar=Menu(top)
file=Menu(menubar,tearoff=0)
file.add_command(label="New File")
file.add_command(label="Save File")
file.add_command(label="Save As")
file.add_command(label="Open File")

menubar.add_cascade(label="Files",menu=file)
top.config(menu=menubar)

nameLabel=Label(top,text="Enter your Name:")
nameEntry=Entry(top)
nameLabel.grid(row=0,column=0)
nameEntry.grid(row=0,column=1)

emailLabel=Label(top,text="Enter email ID:")
emailEntry=Entry(top)
emailLabel.grid(row=1,column=0)
emailEntry.grid(row=1,column=1)

gender=IntVar()
genderLabel=Label(top,text="Select your gender")
genderLabel.grid(row=2,column=0)
maleRadio=Radiobutton(top,text="Male",variable=gender,value=1)
femaleRadio=Radiobutton(top,text="Female",variable=gender,value=2)
maleRadio.grid(row=2,column=1)
femaleRadio.grid(row=2,column=2)

cpp=IntVar()
python=IntVar()
java=IntVar()
langLabel=Label(top,text="Select your languages")
l1=Checkbutton(top,text="C++",onvalue=1,offvalue=0,variable=cpp)
l2=Checkbutton(top,text="python",onvalue=1,offvalue=0,variable=python)
l3=Checkbutton(top,text="java",onvalue=1,offvalue=0,variable=java)
langLabel.grid(row=3,column=0)
l1.grid(row=3,column=1)
l2.grid(row=3,column=2)
l3.grid(row=3,column=3)

listlabel=Label(top,text="select your country")
l=Listbox(top)     #  list for few elements
for i in b:
    l.insert(END,i) 
    
listlabel.grid(row=4,column=0)
l.grid(row=4,column=1)

b=Button(top,text="Submit",command=store_data)
b.grid(row=5,column=0)
ct=Button(top,text="Create Table",command=create_table)
ct.grid(row=5,column=1)
sd=Button(top,text="Show Data",command=show_data)
ud=Button(top,text="Update Data",command=update_data)
ud.grid(row=5,column=3)
sd.grid(row=5,column=2)

top.mainloop()
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkcalendar import *
from tkinter.ttk import Combobox
import mysql.connector
import datetime as dt
def clfield():
    t2.delete(0,END)
    t3.delete(0, END)
    # t4.delete(0, END)
    t5.delete(0, END)
    l7.config(text='')
    l8.config(text='')
def maxrec():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("select max(slno) from deposite")
    mydata = mycur.fetchone()
    if mydata[0] is not None:
        mx = mydata[0]
        mx = mx + 1
    else:
        mx = 1
    t1.delete(0, END)
    t1.insert(0, mx)
    clfield()
def depositerec():
    s1 = t1.get()
    s2 = t2.get()
    s3 = t3.get()
    s4 = t4.get()
    s5=t5.get()
    if s2 == "":
        messagebox.showinfo('Warn....', "Please Enter Slip Date ")
        return

    if s3 == "":
        messagebox.showinfo('Warn....', "Please Enter Applicant Number")
        return

    if s4 == "":
        messagebox.showinfo('Warn....', "Please enter perticular")
        return

    if s5 == "":
        messagebox.showinfo('Warn....', "Please Enter amount")
        return
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur=mydb.cursor()
    mycur.execute("insert into deposite values("+s1+",'"+s2+"','"+s3+"','"+s4+"','"+s5+"')")
    mydb.commit()
    messagebox.showinfo('Confirm',"Amount Sucessfully Deposited......")
    maxrec()
    clfield()

def info(*args):
    s3=t3.get()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("select apname from applicant where apno="+s3)
    dta=mycur.fetchone()
    for i in dta:
        l7.config(text=str(i))

    #openeing
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("select opbal from applicant where apno=" + s3)
    dta=mycur.fetchone()
    for i in dta:
        a=str(i)

    #deposite
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("select sum(amount) from deposite where apno="+s3)
    mydta=mycur.fetchone()
    for i in mydta:
        if i is not None:
            b=str(i)
            c=int(a)-int(b)
            l8.config(text=str(c))
        else:
            l8.config(text=str(a))
def serrec():
    clfield()
    s1 = t1.get()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("select *from deposite where slno=" + s1)
    mydata = mycur.fetchone()
    if mydata is not None:
        t2.insert(0, mydata[1])
        t3.insert(0, mydata[2])
        t4.insert(0, mydata[3])
        t5.insert(0, mydata[4])
    else:
        messagebox.showinfo('confirm', 'Record is not found')
def uprec():
    s1 = t1.get()
    s2 = t2.get()
    s3 = t3.get()
    s4 = t4.get()
    s5 = t5.get()

    if s2 == "":
        messagebox.showinfo('Warn....', "Please Enter Slip Date ")
        return

    if s3 == "":
        messagebox.showinfo('Warn....', "Please Enter Applicant Number")
        return

    if s4 == "":
        messagebox.showinfo('Warn....', "Please enter perticular")
        return

    if s5 == "":
        messagebox.showinfo('Warn....', "Please Enter amount")
        return

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("update deposite set sldate='" + s2 + "',apno='" + s3 + "',perticular='" + s4 + "',amount='" + "' where slno =" + s1)
    mydb.commit()
    messagebox.showinfo('Confirm', "Slip is updated")
    maxrec()

def delrec():
    s1 = t1.get()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    res = messagebox.askyesnocancel('confirm', "Are you sure delete ?")
    if res == True:
        mycur = mydb.cursor()
        mycur.execute("delete from deposite where slno=" + s1)
        mydb.commit()
        messagebox.showinfo('Confirm', 'Rec is deleted')
        maxrec()


def pick_date(event):
    global cal,date_window
    date_window=Toplevel()
    date_window.grab_set()
    date_window.title("Choose Date of Birth")
    date_window.geometry("250x250+530+320")
    cal=Calendar(date_window,selectmode="day",date_pattern="dd/mm/yyyy")
    cal.place(x=0,y=0)

    submit_but=Button(date_window,text="submit",command=grab_date,font=f1)
    submit_but.place(x=70,y=200)
def grab_date():
    t2.delete(0,END)
    t2.insert(0,cal.get_date())
    date_window.destroy()

#particular
global y
y=['CASH','UPI','DD']
global d
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bank"
)
mycur=mydb.cursor()
mycur.execute("select apno from applicant")
data=mycur.fetchall()
d=[]
for i in data:
    d.append(i)

win=Tk()
win.geometry("1000x1000")
win.title("Home Page")
f1=('arial',15,'bold')
f2=('Algerian',25,'bold')
f3=('Rockwell',15,'bold')
# CANVAS
l1=Label(win,text="DEPOSITE",font=f2).place(x=400,y=70)

l2=Label(win,text='Slip Number : ',font=f1).place(x=300,y=140)
t1=Entry(win,bd=2,font=f3)
t1.place(x=500,y=140)

l3=Label(win,text='Slip Date : ',font=f1).place(x=300,y=200)
t2=Entry(win,bd=2,font=f3)
t2.place(x=500,y=200)
t2.insert(0,"dd/mm/yyyy")
t2.bind("<1>",pick_date)

l4=Label(win,text='Applicant Number : ',font=f1).place(x=300,y=260)
t3=Combobox(win,values=d,state='readonly',font=f3)
t3.bind("<<ComboboxSelected>>",info)
t3.place(x=500,y=260)


l5=Label(win,text="Particular : ",font=f1).place(x=300,y=320)
t4=Combobox(win,values=y,font=f3,state='readonly')
t4.place(x=500,y=320)

l6=Label(win,text="Amount : ",font=f1).place(x=300,y=380)
t5=Entry(win,bd=2,font=f3)
t5.place(x=500,y=380)
# info
l9=Label(win,text="Total Deposition =",font=f1)
l9.place(x=400,y=450)
l7=Label(win,text="",font=f1)
l7.place(x=300,y=450)
# deposite history
l8=Label(win,text="",font=f1)
l8.place(x=600,y=450)

b1=Button(win,text="ADD",font=f1,command=maxrec)
b1.place(x=150,y=500)

b2=Button(win,text="DEPOSITE",font=f1,command=depositerec)
b2.place(x=300,y=500)

b3=Button(win,text="SEARCH",font=f1,command=serrec)
b3.place(x=450,y=500)

b4=Button(win,text="UPDATE",font=f1,command=uprec)
b4.place(x=600,y=500)

b5=Button(win,text="CANCEL",font=f1,command=delrec)
b5.place(x=150,y=550)

b6=Button(win,text="EXIT",font=f1,command=win.quit)
b6.place(x=300,y=550)

b7=Button(win,text="CLEAR",font=f1,command=clfield)
b7.place(x=450,y=550)


win.mainloop()
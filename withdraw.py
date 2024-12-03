from tkinter import *
from tkinter import messagebox
from tkcalendar import *
import mysql.connector
from PIL import Image,ImageTk
from tkinter.ttk import Combobox

win=Toplevel()
win.geometry("1000x1000")
win.title("WITHDRAW")
img=Image.open("pic/asd.jpg")
global p
p=['CASH','UPI','DD']

imgp=ImageTk.PhotoImage(img)
imgl=Label(win,image=imgp)
imgl.place(x=0,y=0)
def maxrec():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("select max(slno) from withdraw")
    mydata = mycur.fetchone()
    if mydata[0] is not None:
        mx = mydata[0]
        mx = mx + 1
    else:
        mx = 1
    t1.delete(0, END)
    t1.insert(0, mx)
    # clfield()
def withdraw():
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

    # opening bal
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur=mydb.cursor()
    mycur.execute("select opbal from applicant where apno=" + s3)
    data=mycur.fetchone()
    for i in data:
        a=str(i)

#     after deposition
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur=mydb.cursor()
    mycur.execute("select sum(amount) from deposite where apno="+s3)
    data=mycur.fetchone()
    for i in data:
        if i is not None:
            b=str(i)
            c=int(a)+int(b)
        else:
            c=int(a)
# after transition
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur=mydb.cursor()
    mycur.execute("select sum(amount) from withdraw where apno= "+s3)
    data=mycur.fetchone()
    for i in data:
        if i is not None:
            d=str(i)
            am=int(c)-int (d)
            l7.config(text=str(d))#ld
            l8.config(text=str(am))#lc

            if int(am)>int(s5):
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="bank"
                )
                mycur = mydb.cursor()
                mycur.execute("insert into withdraw values("+s1+",'"+s2+"','"+s3+"','"+s4+"','"+s5+"')")
                mydb.commit()
                messagebox.showinfo('confirm','Amount Withdraw')
                clfield()
            else:
                messagebox.showinfo('confirm','No balance')
        else:
            if int(c)>int(s5):
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="bank"
                )
                mycur = mydb.cursor()
                mycur.execute("insert into withdraw values("+s1+",'"+s2+"','"+s3+"','"+s4+"','"+s5+"')")
                mydb.commit()
                messagebox.showinfo('confirm','Amount withdraw')
                clfield()
            else:
                messagebox.showinfo('confirm','no balance')
def info(*args):
    s3 = t3.get()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("select apname from applicant where apno=" + s3)
    dta = mycur.fetchone()
    for i in dta:
        l10.config(text=str(i))

        # openeing
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("select opbal from applicant where apno=" + s3)
    dta = mycur.fetchone()
    for i in dta:
        a = str(i)

        # deposite
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("select sum(amount) from deposite where apno=" + s3)
    mydta = mycur.fetchone()
    for i in mydta:
        if i is not None:
            b = str(i)
            c = int(a) + int(b)
            # l8.config(text=str(c))
        else:
            c=int(a)
            # l8.config(text=str(a))
#     balance
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("select sum(amount) from withdraw where apno="+s3)
    data=mycur.fetchone()
    for i in data:
        if i is not None:
            d=str(i)
            am=int(c)-int(d)
            l7.config(text=str(d))
            l8.config(text=str(am))
        else:
            l7.config(text='NOne')
            l8.config(text=str(c))

# def insertrec():
#     s3 = t3.get()
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="bank"
#     )
#     mycur = mydb.cursor()
#     mycur.execute("select opbal from applicant where apno=" + s3)
#     mydata = mycur.fetchone()[0]
#     print(mydata)
def clfield():
    t2.delete(0,END)
    t3.delete(0, END)
    t4.delete(0, END)
    t5.delete(0, END)
    l7.config(text='')
    l8.config(text='')
# def saverec():
#     s1 = t1.get()
#     s2 = t2.get()
#     s3 = t3.get()
#     s4 = t4.get()
#     s5=t5.get()
#     if s2 == "":
#         messagebox.showinfo('Warn....', "Please Enter Slip Date ")
#         return
#
#     if s3 == "":
#         messagebox.showinfo('Warn....', "Please Enter Applicant Number")
#         return
#
#     if s4 == "":
#         messagebox.showinfo('Warn....', "Please enter perticular")
#         return
#
#     if s5 == "":
#         messagebox.showinfo('Warn....', "Please Enter amount")
#         return
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="bank"
#     )
#     mycur=mydb.cursor()
#     mycur.execute("insert into deposite values("+s1+",'"+s2+"','"+s3+"','"+s4+"','"+s5+"')")
#     messagebox.showinfo('Confirm',"Record is saved")
#     mycur.execute("select opbal from applicant where apno=" + s3)
#     mydata = int(mycur.fetchone()[0])-int(s5)
#     balance=str(mydata)
#     mycur.execute("update applicant set opbal='"+balance+"' where apno="+s3)
#     mydb.commit()
#     maxrec()
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
    mycur.execute("select *from withdraw where slno=" + s1)
    mydata = mycur.fetchone()
    if mydata is not None:
        t2.insert(0, mydata[1])
        t3.insert(0, mydata[2])
        t4.insert(0, mydata[3])
        t5.insert(0, mydata[4])
    else:
        messagebox.showinfo('confirm', 'Record is not found')

    s3=t3.get()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("select apname from applicant where apno="+s3)
    data=mycur.fetchone()[0]
    l10.config(text=str(data))

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
    mycur.execute("update withdraw set sldate='" + s2 + "',apno='" + s3 + "',perticular='" + s4 + "',amount='" + "' where slno =" + s1)
    mydb.commit()
    # mycur.execute("select opbal from applicant where apno=" + s3)
    # mydata = int(mycur.fetchone()[0]) + int(s5)
    # balance = str(mydata)
    # mycur.execute("update applicant set opbal='" + balance + "' where apno=" + s3)
    # mydb.commit()
    # messagebox.showinfo('Confirm', "Record is updated")
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
    clfield()
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
f1=('arial',15,'bold')
f2=('Algerian',25,'bold')
f3=('Rockwell',15,'bold')


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

l1=Label(win,text="WITHDRAW",font=f2)
l1.place(x=420,y=40)

l2=Label(win,text='Slip Number : ',font=f1)
l2.place(x=300,y=110)
t1=Entry(win,bd=2,font=f3)
t1.place(x=500,y=110)

l3=Label(win,text='Slip Date : ',font=f1)
l3.place(x=300,y=170)
t2=Entry(win,bd=2,font=f3,)
t2.place(x=500,y=170)
t2.insert(0,"dd/mm/yyyy")
t2.bind("<1>",pick_date)

l4=Label(win,text='Applicant Number : ',font=f1)
l4.place(x=300,y=230)
t3=Combobox(win,values=d,state='readonly',font=f3)
t3.bind("<<ComboboxSelected>>",info)
t3.place(x=500,y=230)

l5=Label(win,text="Perticular : ",font=f1)
l5.place(x=300,y=290)
t4=Combobox(win,values=p,font=f3,state='readonly')
t4.place(x=500,y=290)

l6=Label(win,text="Amount : ",font=f1)
l6.place(x=300,y=350)
t5=Entry(win,bd=2,font=f3)
t5.place(x=500,y=350)


# deposite history
l9=Label(win,text="Total Deposition =",font=f1)
l9.place(x=300,y=470)
l8=Label(win,text="",font=f1)
l8.place(x=500,y=470)

l7=Label(win,text="",font=f1)
l7.place(x=500,y=410)
l10=Label(win,text="",font=f1)
l10.place(x=300,y=410)

b1=Button(win,text="ADD",font=f3,command=maxrec,width=9)
b1.place(x=120,y=530)

b2=Button(win,text="WITHDRAW",font=f3,command=withdraw,width=9)
b2.place(x=290,y=530)

b3=Button(win,text="SEARCH",font=f3,command=serrec,width=9)
b3.place(x=460,y=530)

b4=Button(win,text="UPDATE",font=f3,command=uprec,width=9)
b4.place(x=630,y=530)

b5=Button(win,text="CLEAR",font=f3,command=clfield,width=9)
b5.place(x=800,y=530)

b6=Button(win,text="DELETE",font=f3,command=delrec,width=9)
b6.place(x=350,y=590)

b7=Button(win,text="EXIT",font=f3,command=win.quit,width=9)
b7.place(x=600,y=590)
win.mainloop()
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkcalendar import *
import mysql.connector
import datetime as dt
from PIL import ImageTk,Image
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

win=Toplevel()
win.geometry("1000x1000")
win.title("Home Page")
win.resizable(False,False)
img=Image.open("pic/asd.jpg")
imgp=ImageTk.PhotoImage(img)
imgl=Label(win,image=imgp)
imgl.place(x=0,y=0)

def new():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("select max(trno) from interest")
    mydata = mycur.fetchone()
    if mydata[0] is not None:
        mx = mydata[0]
        mx = mx + 1
    else:
        mx = 1
    clean()
    t1.delete(0, END)
    t1.insert(0, mx)

def saverec():
    s1=t1.get()
    s2=t2.get()
    s3=t3.get()
    s4=t4.get()
    s5=t5.get()
    s6=t5.cget("text")
    if s2 == "":
        messagebox.showinfo('Warn....', "Please Enter Transfer Date ")
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
    mycur.execute("insert into interest values("+s1+",'"+s2+"','"+s3+"','"+s4+"','"+s5+"','"+s6+"','"+ls+"')")
    t1.delete(0,END)
    t2.delete(0, END)
    t3.delete(0, END)
    t4.delete(0, END)
    t5.delete(0, END)
    t6.config(text='')
    ls.config(text='')

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
    data=mycur.fetchone()[0]
    ls.config(text=str(data))
    t6.config(text='')

#     opening balance
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("select opbal from applicant where apno="+s3)
    data=mycur.fetchone()
    for i in data:
        a=str(i)

    # after deposition
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("select sum(amount) from deposite")
    data=mycur.fetchone()
    for i in data:
        if i is not None:
            b=str(i)
            c=int(a)+int(b)
        else:
            c=int(a)
    #current
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
            am=int(c)-int (d)
        else:
            am=int(c)
    n=1
    r=2
    si=float(am*n*r)/100
    t6.config(text=str(si))

def serrec():
    t2.delete(0,END)
    t3.delete(0, END)
    t4.delete(0, END)
    t5.delete(0, END)
    t6.config(text="")
    ls.config(text="")

    s1=t1.get()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("select * from interest where trno="+s1)
    data=mycur.fetchone()
    if data is not None:
        t2.insert(0,data[1])
        t3.insert(0,data[2])
        t4.insert(0,data[3])
        t5.insert(0,data[4])
    else:
        messagebox.showinfo('confirm','rec is not found')
    mycur.execute("select interest from interest trno="+s1)
    data=mycur.fetchone()
    t6.config(text=data)
    s3=t3.get()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("select apname from applicant where apno="+s3)
    data=mycur.fetchone()
    for i in data:
        ls.config(text=str(i))

def uprec():
    s1 = t1.get()
    s2 = t2.get()
    s3 = t3.get()
    s4 = t4.get()
    s5 = t5.get()
    s6 = t5.cget("text")
    if s2 == "":
        messagebox.showinfo('Warn....', "Please Enter Transfer Date ")
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
    mycur.execute("update interest set trdate='"+s2+"',apno='"+s3+"',ifrom='"+s4+"',ito='"+s5+"',irate='"+s6+"' where trno="+s1)
    mydb.commit()
    messagebox.showinfo('confirm','interest updates')
    t1.delete(0, END)
    t2.delete(0, END)
    t3.delete(0, END)
    t4.delete(0, END)
    t5.delete(0, END)
    t6.config(text='')
    ls.config(text='')

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
        mycur.execute("delete from interest where trno=" + s1)
        mydb.commit()
        messagebox.showinfo('Confirm', 'Rec is deleted')
        t1.delete(0, END)
        t2.delete(0, END)
        t3.delete(0, END)
        t4.delete(0, END)
        t5.delete(0, END)
        t6.config(text='')
        ls.config(text='')

def clean():
    t1.delete(0, END)
    t2.delete(0, END)
    t3.delete(0, END)
    t4.delete(0, END)
    t5.delete(0, END)
    t6.config(text='')
    ls.config(text='')

f1=('arial',15,'bold')
f2=('Algerian',25,'bold')
f3=('Rockwell',15,'bold')
# for combobox applicant
global p
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
mycur=mydb.cursor()
mycur.execute("select apno from applicant")
data=mycur.fetchall()
p=[]
for i in data:
    p.append(i)


l0=Label(win,text="INTEREST FORM",font=f2)
l0.place(x=370,y=20)

l1=Label(win,text='Transfer Number : ',font=f1)
l1.place(x=300,y=70)
t1=Entry(win,bd=2,font=f3)
t1.place(x=500,y=70)

l2=Label(win,text='Transfer Date : ',font=f1)
l2.place(x=300,y=120)
t2=DateEntry(win,selectmode='day',bd=2,font=f3)
t2.place(x=500,y=120)

l3=Label(win,text='Applicant Number : ',font=f1)
l3.place(x=300,y=170)
t3=Combobox(win,values=p,font=f3)
t3.bind("<<ComboboxSelected>>",info)
t3.place(x=500,y=170)

l4=Label(win,text='Interest from : ',font=f1)
l4.place(x=300,y=220)
t4=DateEntry(win,selectmode='day',bd=2,font=f3)
t4.place(x=500,y=220)

l5=Label(win,text='Interest To : ',font=f1)
l5.place(x=300,y=270)
t5=DateEntry(win,selectmode='day',bd=2,font=f3)
t5.place(x=500,y=270)

l6=Label(win,text='Interest : ',font=f1)
l6.place(x=300,y=320)
t6=Label(win,text='',font=f3)
t6.place(x=500,y=320)

# for info
ls=Label(win,text='',font=f3)
ls.place(x=620,y=320)

b1=Button(win,text="NEW",font=f1,command=new)
b1.place(x=150,y=450)

b2=Button(win,text="INTEREST",font=f1,command=saverec)
b2.place(x=250,y=450)

b3=Button(win,text="SEARCH",font=f1,command=serrec)
b3.place(x=380,y=450)

b4=Button(win,text="UPDATE",font=f1,command=uprec)
b4.place(x=450,y=450)

b5=Button(win,text="CANCEL",font=f1,command=delrec)
b5.place(x=380,y=550)

b6=Button(win,text="EXIT",font=f1,command=win.quit)
b6.place(x=440,y=550)

b7=Button(win,text="CLEAR",font=f1,command=clean)
b7.place(x=540,y=550)

win.mainloop()

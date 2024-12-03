from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkcalendar import *
import mysql.connector
import datetime as dt
from PIL import Image,ImageTk
def clfield():
    t2.delete(0,END)
    t3.delete(0, END)
    t4.delete(0, END)
    t5.config(text="")
def maxrec():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur=mydb.cursor()
    mycur.execute("select max(clno) from closeac")
    mydata=mycur.fetchone()
    if mydata[0] is not None:
        mx=mydata[0]
        mx=mx+1
    else:
        mx=1
    t1.delete(0,END)
    t1.insert(0,mx)
    clfield()
    date = dt.datetime.now()
    t2.insert(0, date)


def saverec():
    s1=t1.get()
    s2=t2.get()
    s3=t3.get()
    s4=t4.get()
    s5=t5.cget()
    if s2=="":
        messagebox.showinfo('Warn....',"Please select date")
        return
    if s3=="":
        messagebox.showinfo('Warn....',"Please Enter applicant number")
        return
    if s4=="":
        messagebox.showinfo('Warn....',"Please Enter Reason ")
        return
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur=mydb.cursor()
    mycur.execute("insert into closeac values("+s1+",'"+s2+"','"+s3+"','"+s4+"','"+s5+"')")
    mydb.commit()
    messagebox.showinfo('Confirm',"Record is saved")
    maxrec()

def serrec():
    s1 = t1.get()
    clfield()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("select *from closeac where clno=" + s1)
    mydata = mycur.fetchone()
    apno = mycur.fetchone()[2]
    if mydata is not None:
        t2.insert(0, mydata[1])
        t3.insert(0, mydata[2])
        t4.insert(0, mydata[3])
    else:
        messagebox.showinfo('confirm', 'Record is not found')
    ap=mydata[2]
    mycur.execute("select opbal from applicant where apno=" +apno)
    mydata1 = mycur.fetchone()[0]
    t5.config(text=mydata1)
    mydb.commit()


def uprec():
    s1 = t1.get()
    s2 = t2.get()
    s3 = t3.get()
    s4 = t4.get()
    s5 = t5.cget()

    if s2 == "":
        messagebox.showinfo('Warn....', "Please Enter customer Name ")
        return
    if s3 == "":
        messagebox.showinfo('Warn....', "Please Enter customer Address ")
        return
    if s4 == "":
        messagebox.showinfo('Warn....', "Please Enter customer City ")
        return

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("update closeac set cldate='" + s2 + "',apno='" + s3+ "',reason='" +s4+ "',ramount='"+s5+"' where clno =" + s1)
    mydb.commit()
    messagebox.showinfo('Confirm', "Record is updated")
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
        mycur.execute("delete from closeac where clno=" + s1)
        mydb.commit()
        messagebox.showinfo('Confirm', 'Rec is deleted')
        maxrec()

win=Toplevel()
win.geometry("1000x1000")
win.title("Home Page")
win.resizable(False,False)
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
img=Image.open("pic/asd.jpg")
imgp=ImageTk.PhotoImage(img)
imgl=Label(win,image=imgp)
imgl.place(x=0,y=0)

l1=Label(win,text="CLOSE ACCOUNT",font=f2)
l1.place(x=370,y=70)

l2=Label(win,text='Close Number : ',font=f1)
l2.place(x=300,y=140)
t1=Entry(win,bd=2,font=f3)
t1.place(x=520,y=140)

l3=Label(win,text='Close Date : ',font=f1)
l3.place(x=300,y=200)
t2=Entry(win,bd=2,font=f3,)
t2.place(x=520,y=200)


l4=Label(win,text='Applicant Number : ',font=f1)
l4.place(x=300,y=260)
t3=Entry(win,bd=2,font=f3)
t3.place(x=520,y=260)

l5=Label(win,text="Reason : ",font=f1)
l5.place(x=300,y=320)
t4=Entry(win,bd=2,font=f3)
t4.place(x=520,y=320)

l6=Label(win,text="Remaining amount  : ",font=f1)
l6.place(x=300,y=380)
t5=Label(win,font=f3)
t5.place(x=520,y=380)


b1=Button(win,text="NEW",font=f3,command=maxrec,width=9)
b1.place(x=250,y=450)
b2=Button(win,text="SAVE",font=f3,command=saverec,width=9)
b2.place(x=450,y=450)
b3=Button(win,text="SEARCH",font=f3,width=9,command=serrec)
b3.place(x=650,y=450)
b4=Button(win,text="UPDATE",font=f3,width=9,command=uprec)
b4.place(x=250,y=520)
b5=Button(win,text="Del",font=f3,width=9,command=delrec)
b5.place(x=450,y=520)
b6=Button(win,text="EXIT",font=f3,command=win.quit,width=9)
b6.place(x=650,y=520)
win.mainloop()
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
    t5.delete(0, END)
    t6.delete(0,END)
    t6.insert(0,"dd/mm/yyyy")
    t7.delete(0,END)
    l9.config(text="")
    cb.delete(0,END)
    t8.delete(0,END)
def newrec():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("select max(apno) from applicant")
    mydata = mycur.fetchone()
    if mydata[0] is not None:
        mx = mydata[0]
        mx = mx + 1
    else:
        mx = 1
    t1.delete(0, END)
    t1.insert(0, mx)
    clfield()

def saverec():
    apno = t1.get()
    apname = t2.get()
    apadd = t3.get()
    city = t4.get()
    contact = t5.get()
    bdate = t6.get()
    age = l9.cget('text')
    gender = cb.get()
    nomini = t7.get()
    opbal = t8.get()
    if apname=="":
        messagebox.showinfo('Warn....', "Please Enter Applicant Name ")
        return

    if apadd == "":
        messagebox.showinfo('Warn....', "Please Enter Applicant Address ")
        return

    if city == "":
        messagebox.showinfo('Warn....', "Please Enter Applicant City ")
        return

    if contact == "":
        messagebox.showinfo('Warn....', "Please Enter Applicant Contact ")
        return

    if bdate == "":
        messagebox.showinfo('Warn....', "Select Applicant Birth Date ")
        return

    if age == "":
         messagebox.showinfo('Warn....', "Select Birth date")
         return

    if gender == "":
        messagebox.showinfo('Warn....', "Select gender ")
        return

    if nomini == "":
        messagebox.showinfo('Warn....', "Please Enter Nomini")
        return

    if opbal == "":
        messagebox.showinfo('Warn....', "Please Enter balance ")
        return

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("insert into applicant values("+apno+",'"+apname+"','"+apadd+"','"+city+"','"+contact+"','"+bdate+"','"+age+"','"+gender+"','"+nomini+"','"+opbal+"')")
    mydb.commit()
    messagebox.showinfo('Confirm',"Record is saved.....")
    clfield()

def searchrec():
    s1 = t1.get()
    clfield()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("select *from applicant where apno=" + s1)
    mydata = mycur.fetchone()
    if mydata is not None:
        t2.insert(0, mydata[1])
        t3.insert(0, mydata[2])
        t4.insert(0, mydata[3])
        t5.insert(0, mydata[4])
        t6.delete(0,END)
        t6.insert(0, mydata[5])
        l9.config(text=mydata[6])
        cb.insert(0, mydata[7])
        t7.insert(0, mydata[8])
        t8.insert(0,mydata[9])
    else:
        messagebox.showinfo('confirm', 'Record is not found')

def  uprec():
    apno = t1.get()
    apname = t2.get()
    apadd = t3.get()
    city = t4.get()
    contact = t5.get()
    bdate = t6.get()
    age = l9.cget('text')
    gender = cb.get()
    nomini = t7.get()
    opbal = t8.get()
    if apname == "":
        messagebox.showinfo('Warn....', "Please Enter Applicant Name ")
        return

    if apadd == "":
        messagebox.showinfo('Warn....', "Please Enter Applicant Address ")
        return

    if city == "":
        messagebox.showinfo('Warn....', "Please Enter Applicant City ")
        return

    if contact == "":
        messagebox.showinfo('Warn....', "Please Enter Applicant Contact ")
        return

    if bdate == "":
        messagebox.showinfo('Warn....', "Select Applicant Birth Date ")
        return

    if age == "":
        messagebox.showinfo('Warn....', "Select Birth date")
        return

    if gender == "":
        messagebox.showinfo('Warn....', "Select gender ")
        return

    if nomini == "":
        messagebox.showinfo('Warn....', "Please Enter Nomini")
        return

    if opbal == "":
        messagebox.showinfo('Warn....', "Please Enter balance ")
        return

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("update applicant set apname='" + apname + "',apadd='" +apadd + "',city='" + city + "',contact='" + contact+"',bdate='"+bdate+"',age='"+age+"',gender='"+gender+"',nomini='"+nomini+"',opbal='"+opbal+"' where apno="+apno)
    mydb.commit()
    messagebox.showinfo('Confirm', "Record is updated")
    newrec()
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
       mycur.execute("delete from applicant where apno=" + s1)
       mydb.commit()
       messagebox.showinfo('Confirm', 'Rec is deleted')
       newrec()


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
    t6.delete(0,END)
    t6.insert(0,cal.get_date())
    date_window.destroy()

    date = cal.get_date()
    date1 = str(date)
    birth_day = date1[0:2]
    birth_month = date1[3:5]
    birth_year = date1[6:10]
    current_day = dt.datetime.today().day
    current_month = dt.datetime.today().month
    current_year = dt.datetime.today().year

    age_day = current_day - int(birth_day)
    age_month = current_month - int(birth_month)
    age_year = current_year - int(birth_year)

    str1 = str(age_day)
    str2 = str(age_month)
    str3 = str(age_year)
    l9.config(text=str3 + " years " + str2 + " month " + str1 + " days")
win=Toplevel()
win.geometry("1000x1000")
win.title("Home Page")
img=Image.open("pic/asd.jpg")
imgp=ImageTk.PhotoImage(img)
imgl=Label(win,image=imgp)
imgl.place(x=0,y=0)

f1=('arial',15,'bold')
f2=('Algerian',25,'bold')
f3=('Rockwell',15,'bold')
l1=Label(win,text="APPLICANT FORM",font=f2)
l1.place(x=370,y=20)

l2=Label(win,text='Applicant Number : ',font=f1)
l2.place(x=300,y=70)
t1=Entry(win,bd=2,font=f3)
t1.place(x=500,y=70)

l3=Label(win,text='Applicant Name : ',font=f1)
l3.place(x=300,y=120)
t2=Entry(win,bd=2,font=f3)
t2.place(x=500,y=120)

l4=Label(win,text='Applicant Address : ',font=f1)
l4.place(x=300,y=170)
t3=Entry(win,bd=2,font=f3)
t3.place(x=500,y=170)

l5=Label(win,text="City : ",font=f1)
l5.place(x=300,y=220)
t4=Entry(win,bd=2,font=f3)
t4.place(x=500,y=220)

l6=Label(win,text="Contact : ",font=f1)
l6.place(x=300,y=270)
t5=Entry(win,bd=2,font=f3)
t5.place(x=500,y=270)

l7=Label(win,text="Birth Date : ",font=f1)
l7.place(x=300,y=320)
t6=Entry(win,bd=2,font=f3,)
t6.place(x=500,y=320)
t6.insert(0,"dd/mm/yyyy")
t6.bind("<1>",pick_date)

l8=Label(win,text="Age : ",font=f1)
l8.place(x=300,y=370)
l9=Label(win,font=f3)
l9.place(x=500,y=370)

l10=Label(win,text="Gender : ",font=f1)
l10.place(x=300,y=420)
data=("Male","Female","Other")
cb=Combobox(win,values=data,font=f3)
cb.place(x=500,y=420)

l11=Label(win,text="Nomini : ",font=f1)
l11.place(x=300,y=470)
t7=Entry(win,bd=2,font=f3)
t7.place(x=500,y=470)

l12=Label(win,text="Opening balance : ",font=f1)
l12.place(x=300,y=520)
t8=Entry(win,bd=2,font=f3)
t8.place(x=500,y=520)

b1=Button(win,text="NEW",font=f1,command=newrec)
b1.place(x=200,y=570)

b2=Button(win,text="SAVE",font=f1,command=saverec)
b2.place(x=300,y=570)

b3=Button(win,text="SEARCH",font=f1,command=searchrec)
b3.place(x=400,y=570)

b4=Button(win,text="UPDATE",font=f1,command=uprec)
b4.place(x=515,y=570)

b5=Button(win,text="Delete",font=f1,command=delrec)
b5.place(x=630,y=570)

b6=Button(win,text="EXIT",font=f1,command=win.quit)
b6.place(x=730,y=570)

win.mainloop()
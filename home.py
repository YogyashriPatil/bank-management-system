from tkinter import *
from PIL import ImageTk
from PIL import Image
def applicantrec():
    import applicant
def depositerec():
    import deposite
def withdrawrec():
    import withdraw
def interestrec():
    import interest
def close():
    import closeac

win=Toplevel()
win.geometry("1000x1000")
win.title("Home Page")
f1=('arial',15,'bold')
f2=('arial',17,'bold')

head=Label(win,text="Home Bank ",bg="yellow",font=('Times New Roman',50,'bold'))
head.pack(fill=X)

img=PhotoImage(file="pic/money.png")
img1= Label(head, image=img,bg="yellow")
img1.place(x=200, y=10)
img2= Label(head, image=img,bg="yellow")
img2.place(x=700, y=10)

bottom= Frame(win, height=80, bg="#fcad03")
bottom.pack(fill=X)

b1=Button(win,text='APPLICANT',font=f2,command=applicantrec)
b1.place(x=70,y=100)
b2=Button(win,text='DEPOSITE',font=f2,command=depositerec)
b2.place(x=240,y=100)
b3=Button(win,text='WITHDRAW',font=f2,command=withdrawrec)
b3.place(x=410,y=100)
b4=Button(win,text='INTEREST',font=f2,command=interestrec)
b4.place(x=590,y=100)
b5=Button(win,text='CLOSE AC',font=f2,command=close)
b5.place(x=750,y=100)

img4=Image.open("pic/homebank.jpg")
# img4.resize((100,100))
imgp=ImageTk.PhotoImage(img4)
imgl=Label(win,image=imgp)
imgl.place(x=0,y=160)
win.mainloop()
from tkinter import *
from tkinter import messagebox
import pyttsx3
from PIL import ImageTk
from PIL import Image
win=Tk()
win.geometry("1000x1000+100+100")
win.title("Login page")
win.config(bg="#1C4088")
engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def checkuser():
    nm=e1.get()
    pw=e2.get()

    if nm=='yogi' and pw=='1234':
        speak("Login sucessfully..")
        import home
    else:
        messagebox.showinfo("Error","Encoreect username and password")
        speak("Encoreect username and password")

f1=('arial',15,'bold')
f2=('arial',17,'bold')

img=Image.open("pic/home.jpg")
img.resize((100,100))
imgp=ImageTk.PhotoImage(img)

imgl=Label(win,image=imgp)
imgl.place(x=70,y=50)

l1=Label(win,text="Login Here",font=('arial',40,'bold'),bg="#3104A0")
l1.place(x=400,y=100)

l2=Label(win,text="Username : ",font=('arial',17,'bold'),bg="#3104A0")
l2.place(x=350,y=200)
e1=Entry(win,bd=3,font=f1)
e1.place(x=500,y=200)

l3=Label(win,text="Password : ",font=('arial',17,'bold'),bg="#3104A0")
l3.place(x=350,y=250)
e2=Entry(win,bd=3,font=f1,show='*')
e2.place(x=500,y=250)

b1=Button(win,text="Login",font=f2,command=checkuser,bg="#AFABA7",width=10)
b1.place(x=350,y=320)

b2=Button(win,text="Cancel",font=f2,command=win.quit,bg="#AFABA7",width=10)
b2.place(x=550,y=320)

win.mainloop()
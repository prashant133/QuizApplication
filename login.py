import tkinter.messagebox
from tkinter import *
from PIL import ImageTk , Image
import sqlite3
from create_an_account import reg
from quiz import start

def login():
    if user_entry.get()=="" and password_entry.get()=="":
        tkinter.messagebox.showinfo("Invalid Details","Invalid email or password")
    elif user_entry.get()=="":
        tkinter.messagebox.showinfo("Invalid Details","Invalid email or password")
    elif password_entry.get()=="":
        tkinter.messagebox.showinfo("Invalid Details","Invalid email or password")
    else:
        connector = sqlite3.connect("registration.db")
        cur = connector.cursor()
        query = "SELECT * FROM Information WHERE email=? and password=?"
        user_name = user_entry.get()
        password_name = password_entry.get()
        cur.execute(query,(user_name,password_name))
        rows = cur.fetchall()
        print(rows)
        #checking whether it is ir not
        if len(rows)>0:
            tkinter.messagebox.showinfo("Login succes","Login has been successful")
            # destroying the root window
            root.destroy()
            start()
        else :
            tkinter.messagebox.showinfo("Invalid Deatils", "Ivalid username or Password")
root = Tk()
root.geometry('400x400')
root.title('Login')
root.resizable(0,0)
root.iconbitmap('Image/key.ico')

#adding the background color
root.config(bg='lightblue')


#images
img1 = ImageTk.PhotoImage(Image.open("Image/user.png"))
img2 = ImageTk.PhotoImage(Image.open("Image/password.png"))



#adding text on the root window
text = Label(root,text="LOGIN",bg='lightblue',font =('consolas',20))
text.grid(row=0,column=2,pady =(20,0))
#creating label for the root window
user = Label(root,image=img1,)
user.grid(row=1,column=1,padx=10,pady=(30,25))
password = Label(root,image = img2)
password.grid(row=2,column=1,padx =10,pady =(25,30))

#creating Entry for the window
user_entry = Entry(root,width=15,font = ('consolas',24))
user_entry.grid(row=1,column=2)
password_entry = Entry(root,width=15,font = ('consolas',24),show="*")
password_entry.grid(row=2,column=2)


#creating button
login_btn = Button(root,text='Login',bg ="lightblue",font =('consolas',15),command = login)
login_btn.grid(row=3,column = 2,pady=10)
create_btn = Button(root,text="Create an Account",bg='lightblue',font=('consolas',15),command = reg)
create_btn.grid(row=4,column =2,pady=10)




mainloop()
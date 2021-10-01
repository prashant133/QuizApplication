import tkinter.messagebox
from tkinter import *
from PIL import ImageTk , Image
import sqlite3

root = Tk()
root.geometry('800x363')
root.title('create an account')
root.resizable(0,0)
root.iconbitmap('Image/key.ico')

bg = ImageTk.PhotoImage(Image.open("Image/laptop.png"))
root.config(bg='lightblue')

my_label = Label(root,image=bg,bg='lightblue')
my_label.pack(side=LEFT,padx=(20,0))

#creating the frame
my_frame = LabelFrame(root,bg='lightblue')
my_frame.pack(pady=46,padx=0)

#adding label into the frame
text = Label(my_frame,text ='create an account',pady=10,font =  ('consolas',16),bg='lightblue')
text.grid(row =0 ,column =2)
firstname = Label(my_frame,text = 'First Name',font =  ('consolas',10),bg='lightblue')
firstname.grid(row = 1 ,column = 1,)
lastname = Label(my_frame,text = 'Last Name',font =  ('consolas',10),bg='lightblue')
lastname.grid(row = 1 ,column = 3)
email= Label(my_frame,text = 'Email Address',font =  ('consolas',10),bg='lightblue')
email.grid(row = 3 ,column = 1)
password = Label(my_frame,text = 'Password',font =  ('consolas',10),bg='lightblue')
password.grid(row = 5 ,column = 1)
confirmpassword = Label(my_frame,text = 'Confirm Password ',font =  ('consolas',10),bg='lightblue')
confirmpassword.grid(row =5 ,column =3 )

#adding entry in the frame
firstname_entry = Entry(my_frame)
firstname_entry.grid(row =2 ,column =1,pady=(0,10))
lastname_entry= Entry(my_frame)
lastname_entry.grid(row =2 ,column =3,padx=10)
email_entry = Entry(my_frame,)
email_entry.grid(row =4 ,column =1,pady=(0,10))
password_entry = Entry(my_frame,show='*')
password_entry.grid(row =6,column =1,pady=(0,10))
confirmpassword_entry = Entry(my_frame,show='*')
confirmpassword_entry.grid(row =6 ,column =3,padx=10)



def register():
    if firstname_entry.get() =="" and lastname_entry.get()== "" and email_entry.get()=="" and password_entry.get()=="" and confirmpassword_entry.get()=="":
        tkinter.messagebox.showinfo("Invalid Details","please fill up the details")
    elif firstname_entry.get() =="" and lastname_entry.get()== "" and email_entry.get()=="" and password_entry.get()=="":
        tkinter.messagebox.showinfo("Invalid Details","confimr pasword")
    elif firstname_entry.get() == "" and lastname_entry.get() == "" and email_entry.get() == "" and confirmpassword_entry.get() == "":
        tkinter.messagebox.showinfo("Invalid Details", "password")
    elif firstname_entry.get() == "" and lastname_entry.get() == "" and password_entry.get() == "" and confirmpassword_entry.get()=="":
        tkinter.messagebox.showinfo("Invalid Details", "email given")
    elif  firstname_entry.get() =="" and email_entry.get()=="" and password_entry.get()=="" and confirmpassword_entry.get()=="":
        tkinter.messagebox.showinfo("Invalid Details","lastname given")
    elif  lastname_entry.get() == "" and email_entry.get() == "" and password_entry.get() == "" and confirmpassword_entry.get() == "":
        tkinter.messagebox.showinfo("Invalid Details", "first name given")
    elif email_entry.get() == "" and password_entry.get() == "" and confirmpassword_entry.get() == "":
        tkinter.messagebox.showinfo("Invalid Details", "first and last are given")
    elif lastname_entry.get() == "" and password_entry.get() == "" and confirmpassword_entry.get() == "":
        tkinter.messagebox.showinfo("Invalid Details", "first and email are given")
    elif  lastname_entry.get()== "" and email_entry.get()=="" and confirmpassword_entry.get()=="":
        tkinter.messagebox.showinfo("Invalid Details","first name and password are given")
    elif   lastname_entry.get()== "" and email_entry.get()=="" and password_entry.get()=="" :
        tkinter.messagebox.showinfo("Invalid Details","first and confirm password are given")
    elif firstname_entry.get() == "" and password_entry.get() == "" and confirmpassword_entry.get() == "":
        tkinter.messagebox.showinfo("Invalid Details", "last and email are given")
    elif  firstname_entry.get() =="" and email_entry.get()=="" and confirmpassword_entry.get()=="":
        tkinter.messagebox.showinfo("Invalid Details","last and password are given")
    elif  firstname_entry.get() =="" and email_entry.get()=="" and password_entry.get()=="":
        tkinter.messagebox.showinfo("Invalid Details","last nad confirm password are given")
    elif  firstname_entry.get() =="" and lastname_entry.get()== "" and confirmpassword_entry.get()=="":
        tkinter.messagebox.showinfo("Invalid Details","email and password are given")
    elif  firstname_entry.get() =="" and lastname_entry.get()== "" and password_entry.get()=="" :
        tkinter.messagebox.showinfo("Invalid Details","email and confirm password are given")
    elif  firstname_entry.get() =="" and lastname_entry.get()== "" and email_entry.get()=="":
        tkinter.messagebox.showinfo("Invalid Details","passwrod and confirm password are given")
    elif firstname_entry.get() =="" and lastname_entry.get()== "":
        tkinter.messagebox.showinfo("Invalid Details","first and last are not given")
    elif firstname_entry.get() =="" and email_entry.get()== "":
        tkinter.messagebox.showinfo("Invalid Details","first and email are not given")
    elif firstname_entry.get() =="" and password_entry.get()== "":
        tkinter.messagebox.showinfo("Invalid Details","first and password are not given")
    elif firstname_entry.get() =="" and confirmpassword_entry.get()== "":
        tkinter.messagebox.showinfo("Invalid Details","first and confirm are not given")
    elif email_entry.get()=="" and lastname_entry.get()== "":
        tkinter.messagebox.showinfo("Invalid Details","email and last are not given")
    elif password_entry.get() =="" and lastname_entry.get()== "":
        tkinter.messagebox.showinfo("Invalid Details","password and last are not given")
    elif confirmpassword_entry.get() =="" and lastname_entry.get()== "":
        tkinter.messagebox.showinfo("Invalid Details","confirm password and last are not given")
    elif email_entry.get() =="" and password_entry.get()== "":
        tkinter.messagebox.showinfo("Invalid Details","email and password are not given")
    elif email_entry.get() =="" and confirmpassword_entry.get()== "":
        tkinter.messagebox.showinfo("Invalid Details","email and confirmpassword are not given")
    elif  firstname_entry.get() =="" :
        tkinter.messagebox.showinfo("Invalid Details","first name not given")
    elif  lastname_entry.get() =="" :
        tkinter.messagebox.showinfo("Invalid Details","last name not given")
    elif  email_entry.get() =="" :
        tkinter.messagebox.showinfo("Invalid Details","email name not given")
    elif  password_entry.get() =="" :
        tkinter.messagebox.showinfo("Invalid Details","password name not given")
    elif  confirmpassword_entry.get() =="" :
        tkinter.messagebox.showinfo("Invalid Details","first confirm password not given")
    elif  password_entry.get() != confirmpassword_entry.get():
        tkinter.messagebox.showinfo("Invalid Details","password doesn't match")
    else :
        #creating a data base
        database = sqlite3.connect('registration.db')
        #creating cursor
        cursor = database.cursor()

        '''
        #creating Table
        cursor.execute("""Create Table Information(
        firstname text,
        lastname text,
        password text, 
        confirmpassword text
        )""")

        database.commit()
        '''
        #inserting data into the table
        cursor.execute("Insert Into Information Values(:firstname,:lastname,:password,:confirmpassword)",
                       {
                           'firstname': firstname_entry.get(),
                           'lastname': lastname_entry.get(),
                           'password': password_entry.get(),
                           'confirmpassword': confirmpassword_entry.get()
                       })
        cursor.execute(("SELECT * ,oid FROM Information"))
        data = cursor.fetchall()
        print(data)
        #commting changes
        database.commit()
        database.close()
        #clear the entry boxes
        firstname_entry.delete(0, END)
        lastname_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)
        confirmpassword_entry.delete(0, END)

        #destory the root window
        root.destroy()
#creating the button
createbutton = Button(my_frame,text ='Create Account',bg='lightblue',command=register)
createbutton.grid(row=7,column=2,pady=(10,20))



mainloop()
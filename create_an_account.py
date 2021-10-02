import tkinter
import tkinter.messagebox
from tkinter import *
from PIL import ImageTk , Image
import sqlite3
def reg():
    root = tkinter.Toplevel()
    root.geometry('800x363')
    root.title('create an account')
    root.resizable(0,0)
    root.iconbitmap('Image/key.ico')

    image1 = ImageTk.PhotoImage(Image.open("Image/laptop.png"))
    root.config(bg='lightblue')

    my_label = Label(root,image=image1,bg='lightblue')
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
            tkinter.messagebox.showinfo("Invalid Details","Please fill up the details")
        elif firstname_entry.get() =="" and lastname_entry.get()== "" and email_entry.get()=="" and password_entry.get()=="":
            tkinter.messagebox.showinfo("Invalid Details","Plesse fill up all the details")
        elif firstname_entry.get() == "" and lastname_entry.get() == "" and email_entry.get() == "" and confirmpassword_entry.get() == "":
            tkinter.messagebox.showinfo("Invalid Details", "Plesse fill up all the details")
        elif firstname_entry.get() == "" and lastname_entry.get() == "" and password_entry.get() == "" and confirmpassword_entry.get()=="":
            tkinter.messagebox.showinfo("Invalid Details", "Plesse fill up all the details")
        elif  firstname_entry.get() =="" and email_entry.get()=="" and password_entry.get()=="" and confirmpassword_entry.get()=="":
            tkinter.messagebox.showinfo("Invalid Details","Plesse fill up all the details")
        elif  lastname_entry.get() == "" and email_entry.get() == "" and password_entry.get() == "" and confirmpassword_entry.get() == "":
            tkinter.messagebox.showinfo("Invalid Details", "Plesse fill up all the details")
        elif email_entry.get() == "" and password_entry.get() == "" and confirmpassword_entry.get() == "":
            tkinter.messagebox.showinfo("Invalid Details", "Plesse fill up all the details")
        elif lastname_entry.get() == "" and password_entry.get() == "" and confirmpassword_entry.get() == "":
            tkinter.messagebox.showinfo("Invalid Details", "Plesse fill up all the details")
        elif  lastname_entry.get()== "" and email_entry.get()=="" and confirmpassword_entry.get()=="":
            tkinter.messagebox.showinfo("Invalid Details","Plesse fill up all the details")
        elif   lastname_entry.get()== "" and email_entry.get()=="" and password_entry.get()=="" :
            tkinter.messagebox.showinfo("Invalid Details","Plesse fill up all the details")
        elif firstname_entry.get() == "" and password_entry.get() == "" and confirmpassword_entry.get() == "":
            tkinter.messagebox.showinfo("Invalid Details", "Plesse fill up all the details")
        elif  firstname_entry.get() =="" and email_entry.get()=="" and confirmpassword_entry.get()=="":
            tkinter.messagebox.showinfo("Invalid Details","Plesse fill up all the details")
        elif  firstname_entry.get() =="" and email_entry.get()=="" and password_entry.get()=="":
            tkinter.messagebox.showinfo("Invalid Details","Plesse fill up all the details")
        elif  firstname_entry.get() =="" and lastname_entry.get()== "" and confirmpassword_entry.get()=="":
            tkinter.messagebox.showinfo("Invalid Details","Plesse fill up all the details")
        elif  firstname_entry.get() =="" and lastname_entry.get()== "" and password_entry.get()=="" :
            tkinter.messagebox.showinfo("Invalid Details","Plesse fill up all the details")
        elif  firstname_entry.get() =="" and lastname_entry.get()== "" and email_entry.get()=="":
            tkinter.messagebox.showinfo("Invalid Details","Plesse fill up all the details")
        elif firstname_entry.get() =="" and lastname_entry.get()== "":
            tkinter.messagebox.showinfo("Invalid Details","Two entries missing,kindly fill up the details")
        elif firstname_entry.get() =="" and email_entry.get()== "":
            tkinter.messagebox.showinfo("Invalid Details","Two entries missing,kindly fill up the details")
        elif firstname_entry.get() =="" and password_entry.get()== "":
            tkinter.messagebox.showinfo("Invalid Details","Two entries missing,kindly fill up the details")
        elif firstname_entry.get() =="" and confirmpassword_entry.get()== "":
            tkinter.messagebox.showinfo("Invalid Details","Two entries missing,kindly fill up the details")
        elif email_entry.get()=="" and lastname_entry.get()== "":
            tkinter.messagebox.showinfo("Invalid Details","Two entries missing,kindly fill up the details")
        elif password_entry.get() =="" and lastname_entry.get()== "":
            tkinter.messagebox.showinfo("Invalid Details","Two entries missing,kindly fill up the details")
        elif confirmpassword_entry.get() =="" and lastname_entry.get()== "":
            tkinter.messagebox.showinfo("Invalid Details","Two entries missing,kindly fill up the details")
        elif email_entry.get() =="" and password_entry.get()== "":
            tkinter.messagebox.showinfo("Invalid Details","Two entries missing,kindly fill up the details")
        elif email_entry.get() =="" and confirmpassword_entry.get()== "":
            tkinter.messagebox.showinfo("Invalid Details","Two entries missing,kindly fill up the details")
        elif  firstname_entry.get() =="" :
            tkinter.messagebox.showinfo("Invalid Details","First name not provided ")
        elif  lastname_entry.get() =="" :
            tkinter.messagebox.showinfo("Invalid Details","Last name not provided")
        elif  email_entry.get() =="" :
            tkinter.messagebox.showinfo("Invalid Details","Email not provided")
        elif  password_entry.get() =="" :
            tkinter.messagebox.showinfo("Invalid Details","Password not provided")
        elif  confirmpassword_entry.get() =="" :
            tkinter.messagebox.showinfo("Invalid Details","Password has not been confirm")
        elif  password_entry.get() != confirmpassword_entry.get():
            tkinter.messagebox.showinfo("Invalid Details","password doesn't match")
        else :
            #creating a data base
            database = sqlite3.connect('registration.db')
            #creating cursor
            cursor = database.cursor()


            #creating Table
            cursor.execute("""Create Table Information(
            firstname text,
            lastname text,
            email text,
            password text, 
            confirmpassword text
            )""")
    
            database.commit()

            #inserting data into the table
            cursor.execute("Insert Into Information Values(:firstname,:lastname,:email,:password,:confirmpassword)",
                           {
                               'firstname': firstname_entry.get(),
                               'lastname': lastname_entry.get(),
                               'email': email_entry.get(),
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

            tkinter.messagebox.showinfo("Register","Register complete")

            #destory the root window
            root.destroy()
    #creating the button
    createbutton = Button(my_frame,text ='Create Account',bg='lightblue',command=register)
    createbutton.grid(row=7,column=2,pady=(10,20))



    mainloop()
from tkinter import *
from PIL import ImageTk , Image

root = Tk()
root.geometry('577x263')
root.title('create an account')
root.resizable(0,0)
root.iconbitmap('Image/key.ico')

bg = ImageTk.PhotoImage(Image.open("Image/laptop.png"))
root.config(bg='lightblue')

my_label = Label(root,image=bg,bg='lightblue')
my_label.pack(side=LEFT)

#creating the frame
my_frame = LabelFrame(root,)
my_frame.pack()

#adding label into the frame
text = Label(my_frame,text ='create an account',pady=10)
text.grid(row =0 ,column =2)

firstname = Label(my_frame,text = 'First Name',)
firstname.grid(row = 1 ,column = 1,)
lastname = Label(my_frame,text = 'Last Name')
lastname.grid(row = 1 ,column = 3)
email= Label(my_frame,text = 'Email Address')
email.grid(row = 3 ,column = 1)
password = Label(my_frame,text = 'Password')
password.grid(row = 5 ,column = 1)
confirmpassword = Label(my_frame,text = 'Confirm Password ')
confirmpassword.grid(row =5 ,column =3 )

firstname_entry = Entry(my_frame)
firstname_entry.grid(row =2 ,column =1,pady =10,)
lastname_entry= Entry(my_frame)
lastname_entry.grid(row =2 ,column =3,pady=10,padx=10)
email_entry = Entry(my_frame,)
email_entry.grid(row =4 ,column =1,pady=10,)
password_entry = Entry(my_frame)
password_entry.grid(row =6,column =1,pady=10,)
confirmpassword_entry = Entry(my_frame)
confirmpassword_entry.grid(row =6 ,column =3,pady=10,padx=10)

#creating the button
createbutton = Button(my_frame,text ='Create Account')
createbutton.grid(row=7,column=2,pady=(10,10))





mainloop()
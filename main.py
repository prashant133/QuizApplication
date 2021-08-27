from tkinter import *
from PIL import ImageTk , Image

def startispressed():
    label_img.destroy()
    label_text.destroy()
    lblrules.destroy()
    lbl_instruction.destroy()
    btn_start.destroy()

#creating the root window
root = Tk()

#giving the title for the project
root.title("Quizstar")

#setting the geometry for the rootwindow
root.geometry("700x600")
root.resizable(0,0)

#putting the image in the root window
img1 =ImageTk.PhotoImage(Image.open("gradhat.jpg"))
label_img = Label(root,image= img1)
label_img.pack(pady=(40,0))

#creating the label text
label_text = Label(
    root,
    text = "Quizstar",
    font = ("Comic sans MS",24,"bold")
)
label_text.pack(pady =(0,40))

#putting the image for the button
img2 = ImageTk.PhotoImage(Image.open("start.jpg"))

btn_start = Button(
    root,
    image = img2,
    relief = "flat",
    border = 0,
    background ="#ffffff",
    height=60,
    width = 180,
    command = startispressed,
)
btn_start.pack()

#creating the label for text
lbl_instruction = Label(
    root,
    text = "Read the Rules and\n click start once your are ready",
    background = "#ffffff",
     font = ("consolas",14),
    justify = "center"
)
lbl_instruction.pack(pady=(10,120))

#creating label for the rules
lblrules = Label(
    root,
    text="this quiz contain a question\nyou will get 20 sec",
    width= 100,
    font = ("Times",14),
    background = "#000000",
    foreground = "#FACA2F",
)
lblrules.pack()




mainloop()
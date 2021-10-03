
from tkinter import *
from PIL import ImageTk, Image
import random


def start():
    global ques
    ques = 1
    question = [
        "How do you write COMMENTS in python code?",
        "Which one is NOT a legal variable name?",
        "How do you create a variable with the numeric value 5?",
        "What is the correct file extension for Python files?",
        "How do your create variable with floating number 2.8 ?",
        "What is the correct syntax to output the type of a variable or object in Python ?",
        "What is the correct way to create a function in Python? ?",
        "Which method can be used to remove any whitespace from both the beginning and the end of a string? ?",
        "Which method can be used to return a string in upper case letters?",
        "Which method can be used to replace parts of a string? ?",
    ]

    answer_choice = [
        ["#This is comment", "/*This is comment*/", "//This is a comment", "//This is a comment//"],
        ["Myvar", "_myvar", "my-var", "my_var"],
        ["x=5", "x=int(5)", "Both a and b ", "None"],
        [".pyth", ".pyt", ".pt", ".py"],
        ["x=float(2.8)", "x=2.8", "Both a and b ", "None"],
        ["print(typeof(x))", "print(type(x))", "print(typeof x)", "print(typeOf(x))"],
        ["function myfunction():", "create myFunction():", "DEF myFunction():  ", "def myFunction():  "],
        ["strip()  ", "trim()", "len()", "ptrim()"],
        ["upperCase()", "upper()  ", "uppercase()", "toUpperCase()"],
        ["replaceString()", "switch()", "repl()", "replace()  "],
    ]

    answers = [0, 2, 2, 3, 2, 1, 3, 0, 1, 3]

    user_answer = []
    indexes = []

    def gen():

        while (len(indexes) < 5):
            x = random.randint(0, 9)
            if x in indexes:
                continue
            else:
                indexes.append(x)

    def showresult(score):
        lblQuestion.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()
        labelimage = Label(
            root,
            background='#ffffff',
            border=0

        )
        labelimage.pack(pady=(50, 20))
        labelresulttext = Label(
            root,
            font=("consolas", 20),
            background='#ffffff'
        )
        labelresulttext.pack()
        if score >= 20:
            img = ImageTk.PhotoImage(Image.open("Image/great.png"))
            labelimage.config(image=img,bg="lightblue")
            labelimage.image = img
            labelresulttext.config(text=f"YOU ARE EXCELLENT,your score is {score}",bg='lightblue')


        elif (score > 10 and score < 20):
            img = ImageTk.PhotoImage(Image.open("Image/good.png"))
            labelimage.config(image=img,bg="lightblue")
            labelimage.image = img
            labelresulttext.config(text=f"YOU ARE GOOD,your score is {score}",bg='lightblue')
        else:
            img = ImageTk.PhotoImage(Image.open("Image/sad.png"))
            labelimage.config(image=img,bg='lightblue')
            labelimage.image = img
            labelresulttext.config(text=f"BETTER LUCK NEXT TIME,your score is {score}",bg='lightblue')

    def calc():

        x = 0
        score = 0
        for i in indexes:
            if user_answer[x] == answers[i]:
                score = score + 5
            x += 1
        #print(score)
        showresult(score)



    def selected():
        global radiovar, ques
        global lblQuestion, r1, r2, r3, r4

        x = radiovar.get()
        # print(x) shows the selected radiobutton
        user_answer.append(x)
        radiovar.set(-1)
        if ques < 5:
            lblQuestion.config(text=question[indexes[ques]])
            r1['text'] = answer_choice[indexes[ques]][0]
            r2['text'] = answer_choice[indexes[ques]][1]
            r3['text'] = answer_choice[indexes[ques]][2]
            r4['text'] = answer_choice[indexes[ques]][3]
            ques += 1
        else:
            # print('indexes')
            # print(user_answer)
            calc()

    def startquiz():
        global lblQuestion, r1, r2, r3, r4,img
        #img = ImageTk.PhotoImage(Image.open("Image/quizbg.jpg"))

        #labl = Label(root, image=img)
        #labl.pack()

        lblQuestion = Label(
            root,
            text=question[indexes[0]],
            font=('consolas', 16),
            width=500,
            justify="center",
            wraplength=400,
            background="lightblue",

        )
        lblQuestion.pack(pady=(100, 40))
        global radiovar
        radiovar = IntVar()
        radiovar.set(-1)  # defult value which will not check the button at first

        r1 = Radiobutton(
            root,
            text=answer_choice[indexes[0]][0],
            font=('Times', 12),
            value=0,  #
            variable=radiovar,
            command=selected,
            background="lightblue",
        )
        r1.pack(pady=5)

        r2 = Radiobutton(
            root,
            text=answer_choice[indexes[0]][1],
            font=('Times', 12),
            value=1,
            variable=radiovar,
            command=selected,
            background="lightblue",
        )
        r2.pack(pady=5)

        r3 = Radiobutton(
            root,
            text=answer_choice[indexes[0]][2],
            font=('Times', 12),
            value=2,
            variable=radiovar,
            command=selected,
            background="lightblue",
        )
        r3.pack(pady=5)
        r4 = Radiobutton(
            root,
            text=answer_choice[indexes[0]][3],
            font=('Times', 12),
            value=3,
            variable=radiovar,
            command=selected,
            background="lightblue",
        )
        r4.pack(pady=5)

    def startispressed():
        label_img.destroy()
        label_text.destroy()
        lblrules.destroy()
        lbl_instruction.destroy()
        btn_start.destroy()
        root.config(bg='lightblue')
        gen()
        startquiz()

    # creating the root window
    root = Tk()

    # giving the title for the project
    root.title("Quizstar")

    # setting the geometry for the rootwindow
    root.geometry("700x600")
    root.resizable(0, 0)

    # giving the image for the window
    root.iconbitmap('Image/quiz.ico')

    # applying the color for the background
    root.config(background='#ffffff')

    # putting the image in the root window
    img1 = ImageTk.PhotoImage(Image.open("Image/gradhat.jpg"))
    label_img = Label(root,
                      image=img1,
                      background=("#000000")
                      )
    label_img.pack(pady=(40, 0))

    # creating the label text
    label_text = Label(
        root,
        text="Quizstar",
        font=("Comic sans MS", 24, "bold"),
        background=("#ffffff")

    )
    label_text.pack(pady=(0, 40))

    # putting the image for the button
    img2 = ImageTk.PhotoImage(Image.open("Image/start.jpg"))

    btn_start = Button(
        root,
        image=img2,
        relief="flat",
        border=0,
        background="#ffffff",
        height=60,
        width=180,
        command=startispressed,
    )
    btn_start.pack()

    # creating the label for text
    lbl_instruction = Label(
        root,
        text="Read the Rules and\n click start once your are ready",
        background="#ffffff",
        font=("consolas", 14),
        justify="center"
    )
    lbl_instruction.pack(pady=(10, 120))

    # creating label for the rules
    lblrules = Label(
        root,
        text="This quiz contain five question\n",
        width=100,
        font=("Times", 14),
        background="#000000",
        foreground="#FACA2F",
    )
    lblrules.pack()

    mainloop()

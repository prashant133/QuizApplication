from tkinter import *
from PIL import ImageTk , Image
import random

question = [
    "this is sample question 1 ?",
    "this is sample question 2 ?",
    "this is sample question 3 ?",
    "this is sample question 4 ?",
    "this is sample question 5 ?",
    "this is sample question 6 ?",
    "this is sample question 7 ?",
    "this is sample question 8 ?",
    "this is sample question 9 ?",
    "this is sample question 10 ?",
]

answer_choice = [
    ["1","2","3","4"],
    ["1","2","3","4"],
    ["1","2","3","4"],
    ["1","2","3","4"],
    ["1","2","3","4"],
    ["1","2","3","4"],
    ["1","2","3","4"],
    ["1","2","3","4"],
    ["1","2","3","4"],
    ["1","2","3","4"],
    ["1","2","3","4"],
]

answers = [0,0,0,0,0,0,0,0,0,0]

user_answer = []
indexes = []
def gen():
    global indexes
    while(len(indexes)<5):
        x = random.randint(0,9)
        if x in indexes :
            continue
        else :
            indexes.append(x)
    #print(indexes)

def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background = '#ffffff',
        border = 0

 )
    labelimage.pack(pady=(50,20))
    labelresulttext = Label(
        root,
        font = ("consolas",20),
        background='#ffffff'
)
    labelresulttext.pack()
    if score >=20:
        img = ImageTk.PhotoImage(Image.open("great.png"))
        labelimage.config(image=img)
        labelimage.image = img
        labelresulttext.config(text = "YOU ARE EXCELLENT")

    elif (score >10 and score < 20):
        img = ImageTk.PhotoImage(Image.open("good.png"))
        labelimage.config(image=img)
        labelimage.image = img
        labelresulttext.config(text="YOU ARE GOOD")
    else:
        img = ImageTk.PhotoImage(Image.open("sad.png"))
        labelimage.config(image=img)
        labelimage.image = img
        labelresulttext.config(text="BETTER LUCK NEXT TIME")
def calc():
    global indexes ,user_answer,answers
    x = 0
    score = 0
    for i in indexes :
        if user_answer[x] == answers[i]:
            score = score+ 5
        x +=1
    print(score)
    showresult(score)
ques =1
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    #print(x) shows the selected radiobutton
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 5 :
        lblQuestion.config(text=question[indexes[ques]])
        r1['text']= answer_choice[ques][0]
        r2['text'] = answer_choice[ques][1]
        r3['text'] = answer_choice[ques][2]
        r4['text'] = answer_choice[ques][3]
        ques += 1
    else :
        print('indexes')
        print(user_answer)
        calc()

def startquiz():
    global lblQuestion,r1,r2,r3,r4
    lblQuestion = Label(
        root,
        text = question[indexes[0]],
        font = ('consolas',16),
        width = 500 ,
        justify = "center",
        wraplength = 400 ,
        background = "#ffffff",

    )
    lblQuestion.pack(pady=(100,40))
    global radiovar
    radiovar = IntVar()
    radiovar.set(-1) #defult value which will not check the button at first

    r1 = Radiobutton(
        root,
        text = answer_choice[indexes[0]][0],
        font = ('Times',12),
        value = 0, #
        variable = radiovar,
        command = selected,
        background="#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text=answer_choice[indexes[0]][1],
        font=('Times', 12),
        value=1,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text=answer_choice[indexes[0]][2],
        font=('Times', 12),
        value=2,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r3.pack(pady=5)
    r4 = Radiobutton(
        root,
        text=answer_choice[indexes[0]][3],
        font=('Times', 12),
        value=3,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r4.pack(pady=5)


def startispressed():
    label_img.destroy()
    label_text.destroy()
    lblrules.destroy()
    lbl_instruction.destroy()
    btn_start.destroy()
    gen()
    startquiz()

#creating the root window
root = Tk()

#giving the title for the project
root.title("Quizstar")

#setting the geometry for the rootwindow
root.geometry("700x600")
root.resizable(0,0)

#giving the image for the window
root.iconbitmap('quiz.ico')

#applying the color for the background
root.config(background='#ffffff')

#putting the image in the root window
img1 =ImageTk.PhotoImage(Image.open("gradhat.jpg"))
label_img = Label(root,
                  image= img1,
                  background = ("#000000")
)
label_img.pack(pady=(40,0))

#creating the label text
label_text = Label(
    root,
    text = "Quizstar",
    font = ("Comic sans MS",24,"bold"),
    background = ("#ffffff")

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
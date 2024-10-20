from tkinter import *
from tkinter import font
i=0
def click1(event):
    global i
    if btn1["text"]==" ":
        i+=1
        if i % 2 == 0:
            btn1["text"],btn1["fg"] = "x","#0000ff"
            move["text"],move["fg"] = "o","#ff0000"
        else:
            btn1["text"],btn1["fg"] = "o","#ff0000"
            move["text"],move["fg"] = "x","#0000ff"
def click2(event):
    global i
    if btn2["text"] == " ":
        i += 1
        if i % 2 == 0:
            btn2["text"], btn2["fg"] = "x", "#0000ff"
            move["text"], move["fg"] = "o", "#ff0000"
        else:
            btn2["text"], btn2["fg"] = "o", "#ff0000"
            move["text"], move["fg"] = "x", "#0000ff"
def click3(event):
    global i
    if btn3["text"] == " ":
        i += 1
        if i % 2 == 0:
            btn3["text"], btn3["fg"] = "x", "#0000ff"
            move["text"], move["fg"] = "o", "#ff0000"
        else:
            btn3["text"], btn3["fg"] = "o", "#ff0000"
            move["text"], move["fg"] = "x", "#0000ff"
def click4(event):
    global i
    if btn4["text"] == " ":
        i += 1
        if i % 2 == 0:
            btn4["text"], btn4["fg"] = "x", "#0000ff"
            move["text"], move["fg"] = "o", "#ff0000"
        else:
            btn4["text"], btn4["fg"] = "o", "#ff0000"
            move["text"], move["fg"] = "x", "#0000ff"
def click5(event):
    global i
    if btn5["text"] == " ":
        i += 1
        if i % 2 == 0:
            btn5["text"], btn5["fg"] = "x", "#0000ff"
            move["text"], move["fg"] = "o", "#ff0000"
        else:
            btn5["text"], btn5["fg"] = "o", "#ff0000"
            move["text"], move["fg"] = "x", "#0000ff"
def click6(event):
    global i
    if btn6["text"] == " ":
        i += 1
        if i % 2 == 0:
            btn6["text"], btn6["fg"] = "x", "#0000ff"
            move["text"], move["fg"] = "o", "#ff0000"
        else:
            btn6["text"], btn6["fg"] = "o", "#ff0000"
            move["text"], move["fg"] = "x", "#0000ff"
def click7(event):
    global i
    if btn7["text"] == " ":
        i += 1
        if i % 2 == 0:
            btn7["text"], btn7["fg"] = "x", "#0000ff"
            move["text"], move["fg"] = "o", "#ff0000"
        else:
            btn7["text"], btn7["fg"] = "o", "#ff0000"
            move["text"], move["fg"] = "x", "#0000ff"
def click8(event):
    global i
    if btn8["text"] == " ":
        i += 1
        if i % 2 == 0:
            btn8["text"], btn8["fg"] = "x", "#0000ff"
            move["text"], move["fg"] = "o", "#ff0000"
        else:
            btn8["text"], btn8["fg"] = "o", "#ff0000"
            move["text"], move["fg"] = "x", "#0000ff"
def click9(event):
    global i
    if btn9["text"] == " ":
        i += 1
        if i % 2 == 0:
            btn9["text"], btn9["fg"] = "x", "#0000ff"
            move["text"], move["fg"] = "o", "#ff0000"
        else:
            btn9["text"], btn9["fg"] = "o", "#ff0000"
            move["text"], move["fg"] = "x", "#0000ff"
root=Tk()
root.title("Крестики и нолики")
root.geometry("800x750")
grid=[""]*10
fr = Frame(root, bg="#606060",borderwidth=5,relief="ridge")
fr.place(relx=0.5,rely=0.55,relheight=0.47,relwidth=0.47,anchor="center")
font1=font.Font(family="Times New Roman", size = 35)
font2=font.Font(family="Corbel Light", size = 75)
move = Label(root,text="o",font=font2,fg="#ff0000")
move.place(relx=0.5,rely=0.19,anchor="center")
movetxt = Label(root,text="Текущий ход:",font=font1)
movetxt.place(relx=0.5,rely=0.1,anchor="center")
btn1=Button(master=fr,width=13,height=6,text=" ",font="Arial 10")
btn2=Button(master=fr,width=13,height=6,text=" ",font="Arial 10")
btn3=Button(master=fr,width=13,height=6,text=" ",font="Arial 10")
btn4=Button(master=fr,width=13,height=6,text=" ",font="Arial 10")
btn5=Button(master=fr,width=13,height=6,text=" ",font="Arial 10")
btn6=Button(master=fr,width=13,height=6,text=" ",font="Arial 10")
btn7=Button(master=fr,width=13,height=6,text=" ",font="Arial 10")
btn8=Button(master=fr,width=13,height=6,text=" ",font="Arial 10")
btn9=Button(master=fr,width=13,height=6,text=" ",font="Arial 10")
for x,y,btn,side,click in [0,0,btn1,"nw",click1],[0.5,0,btn2,"n",click2],[1,0,btn3,"ne",click3],[0,0.5,btn4,"w",click4],[0.5,0.5,btn5,"center",click5]\
        ,[1,0.5,btn6,"e",click6],[0,1,btn7,"sw",click7],[0.5,1,btn8,"s",click8],[1,1,btn9,"se",click9]:
    btn.place(anchor=side,relx=x,rely=y)
    btn.bind("<ButtonPress>",click)
root.mainloop()
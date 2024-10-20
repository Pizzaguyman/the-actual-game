from tkinter import *
from tkinter import font
i=0
def click1(event):
    global i
    if btn1["text"]==" ":
        i+=1
        btn1["text"]="0"
def click2(event):
    global i
    if btn2["text"] == " ":
        i += 1
        btn2["text"]="0"
def click3(event):
    global i
    if btn3["text"] == " ":
        i += 1
        btn3["text"]="0"
def click4(event):
    global i
    if btn4["text"] == " ":
        i += 1
        btn4["text"]="0"
def click5(event):
    global i
    if btn5["text"] == " ":
        i += 1
        btn5["text"]="0"
def click6(event):
    global i
    if btn6["text"] == " ":
        i += 1
        btn6["text"]="0"
def click7(event):
    global i
    if btn7["text"] == " ":
        i += 1
        btn7["text"]="0"
def click8(event):
    global i
    if btn8["text"] == " ":
        i += 1
        btn8["text"]="0"
def click9(event):
    global i
    if btn9["text"] == " ":
        i += 1
        btn9["text"]="0"
root=Tk()
root.title("Крестики и нолики")
root.geometry("800x750")
grid=[""]*10
fr = Frame(root, bg="#606060",borderwidth=5,relief="ridge")
fr.place(relx=0.5,rely=0.5,relheight=0.45,relwidth=0.42,anchor="center")
font1=font.Font(family="Times New Roman", size = 35)
font2=font.Font(family="Corbel Light", size = 75)
move = Label(root,text="",font=font2,fg="#ff0000").place(relx=0.5,rely=0.15,anchor="center")
movetxt = Label(root,text="Текущий ход:",font=font1).place(relx=0.5,rely=0.07,anchor="center")
btn1=Button(master=fr,width=13,height=6,text=" ")
btn2=Button(master=fr,width=13,height=6,text=" ")
btn3=Button(master=fr,width=13,height=6,text=" ")
btn4=Button(master=fr,width=13,height=6,text=" ")
btn5=Button(master=fr,width=13,height=6,text=" ")
btn6=Button(master=fr,width=13,height=6,text=" ")
btn7=Button(master=fr,width=13,height=6,text=" ")
btn8=Button(master=fr,width=13,height=6,text=" ")
btn9=Button(master=fr,width=13,height=6,text=" ")
for x,y,btn,side,click in [0,0,btn1,"nw",click1],[0.5,0,btn2,"n",click2],[1,0,btn3,"ne",click3],[0,0.5,btn4,"w",click4],[0.5,0.5,btn5,"center",click5]\
        ,[1,0.5,btn6,"e",click6],[0,1,btn7,"sw",click7],[0.5,1,btn8,"s",click8],[1,1,btn9,"se",click9]:
    btn.place(anchor=side,relx=x,rely=y)
    btn.bind("<ButtonPress>",click)
root.mainloop()
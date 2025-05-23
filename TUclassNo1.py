import ctypes
import tkinter as tk
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass

MainWin=tk.Tk()
MainWin.geometry("460x620")
MainWin.resizable(width=False,height=False)
MainWin.title("○✕ゲーム 現在：先攻○")
TRUN=0
ManageList=[[0,0,0],[0,0,0],[0,0,0]]
#texts
text11="-"
text12="-"
text13="-"
text21="-"
text22="-"
text23="-"
text31="-"
text32="-"
text33="-"
#switchs
switch11=True
switch12=True
switch13=True
switch21=True
switch22=True
switch23=True
switch31=True
switch32=True
switch33=True
switchF=False
#defs
def ButtonAction():
    global TRUN,ButtonR
    global switch11,switch12,switch13,switch21,switch22,switch23,switch31,switch32,switch33,switchF
    # MLs
    ML11=ManageList[0][0]
    ML12=ManageList[0][1]
    ML13=ManageList[0][2]
    ML21=ManageList[1][0]
    ML22=ManageList[1][1]
    ML23=ManageList[1][2]
    ML31=ManageList[2][0]
    ML32=ManageList[2][1]
    ML33=ManageList[2][2]
    # sums
    global sum1,sum2,sum3,sum4,sum5,sum6,sum7,sum8
    sum1=abs(ML11+ML12+ML13)# 1 123
    sum2=abs(ML21+ML22+ML23)# 2 123
    sum3=abs(ML31+ML32+ML33)# 3 123
    sum4=abs(ML11+ML21+ML31)# 123 1
    sum5=abs(ML12+ML22+ML32)# 123 2
    sum6=abs(ML13+ML23+ML33)# 123 3
    sum7=abs(ML11+ML22+ML33)# 123 123
    sum8=abs(ML31+ML22+ML13)# 123 123
    #print(sum1, sum2, sum3, sum4, sum5, sum6, sum7, sum8)
    if sum1==3:
        switchF=True
        Button11.config(bg="yellow")
        Button12.config(bg="yellow")
        Button13.config(bg="yellow")
        #print("True1")
        #print(sum1)
        if TRUN == 0:
            LabelM.config(text="○の勝ち")
        elif TRUN == 1:
            LabelM.config(text="✕の勝ち")
        LabelM.pack(side = tk.RIGHT)
    if sum2==3:
        switchF = True
        Button21.config(bg="yellow")
        Button22.config(bg="yellow")
        Button23.config(bg="yellow")
        #print("True2")
        #print(sum2)
        if TRUN == 0:
            LabelM.config(text="○の勝ち")
        elif TRUN == 1:
            LabelM.config(text="✕の勝ち")
        LabelM.pack(side = tk.RIGHT)
    if sum3==3:
        switchF = True
        Button31.config(bg="yellow")
        Button32.config(bg="yellow")
        Button33.config(bg="yellow")
        #print("True3")
        #print(sum3)
        if TRUN == 0:
            LabelM.config(text="○の勝ち")
        elif TRUN == 1:
            LabelM.config(text="✕の勝ち")
        LabelM.pack(side = tk.RIGHT)
    if sum4==3:
        switchF = True
        Button11.config(bg="yellow")
        Button21.config(bg="yellow")
        Button31.config(bg="yellow")
        #print("True4")
        #print(sum4)
        if TRUN == 0:
            LabelM.config(text="○の勝ち")
        elif TRUN == 1:
            LabelM.config(text="✕の勝ち")
        LabelM.pack(side = tk.RIGHT)
    if sum5==3:
        switchF = True
        Button12.config(bg="yellow")
        Button22.config(bg="yellow")
        Button32.config(bg="yellow")
        #print("True5")
        #print(sum5)
        if TRUN == 0:
            LabelM.config(text="○の勝ち")
        elif TRUN == 1:
            LabelM.config(text="✕の勝ち")
        LabelM.pack(side = tk.RIGHT)
    if sum6==3:
        switchF = True
        Button13.config(bg="yellow")
        Button23.config(bg="yellow")
        Button33.config(bg="yellow")
        #print("True6")
        #print(sum6)
        if TRUN == 0:
            LabelM.config(text="○の勝ち")
        elif TRUN == 1:
            LabelM.config(text="✕の勝ち")
        LabelM.pack(side = tk.RIGHT)
    if sum7==3:
        switchF = True
        Button11.config(bg="yellow")
        Button22.config(bg="yellow")
        Button33.config(bg="yellow")
        #print("True7")
        #print(sum7)
        if TRUN == 0:
            LabelM.config(text="○の勝ち")
        elif TRUN == 1:
            LabelM.config(text="✕の勝ち")
        LabelM.pack(side = tk.RIGHT)
    if sum8==3:
        switchF = True
        Button31.config(bg="yellow")
        Button22.config(bg="yellow")
        Button13.config(bg="yellow")
        #print("True8")
        #print(sum8)
        if TRUN == 0:
            LabelM.config(text="○の勝ち")
        elif TRUN == 1:
            LabelM.config(text="✕の勝ち")
        LabelM.pack(side = tk.RIGHT)
    else:
        pass
    if switchF == True:
        switch11=False
        switch12=False
        switch13=False
        switch21=False
        switch22=False
        switch23=False
        switch31=False
        switch32=False
        switch33=False
        ButtonR.pack()
        #print("false")
    elif switch11==False:
        if switch12==False:
            if switch13==False:
                if switch21==False:
                    if switch22==False:
                        if switch23==False:
                            if switch31==False:
                                if switch32==False:
                                    if switch33==False:
                                        LabelM.config(text="引き分け")
                                        LabelM.pack(side=tk.RIGHT)
                                        ButtonR.pack()

    else:
        pass
    if TRUN == 0:
        TRUN = 1
    elif TRUN == 1:
        TRUN = 0
    #print(TRUN)
def ButtonAction11():
    global TRUN
    global text11
    global switch11
    if switch11==True:
        if TRUN==0:
            Button11.config(text="〇",fg="red")
            ManageList[0][0]=1
            MainWin.title("○✕ゲーム 現在：後攻✕")
        if TRUN==1:
            Button11.config(text="✕",fg="blue")
            ManageList[0][0]=-1
            MainWin.title("○✕ゲーム 現在：先攻○")
        else:
            pass
        switch11=False
        ButtonAction()
    else:
        pass
def ButtonAction12():
    global TRUN
    global text12
    global switch12
    if switch12==True:
        if TRUN==0:
            Button12.config(text="〇",fg="red")
            ManageList[0][1]=1
            MainWin.title("○✕ゲーム 現在：後攻✕")
        if TRUN==1:
            Button12.config(text="✕",fg="blue")
            ManageList[0][1]=-1
            MainWin.title("○✕ゲーム 現在：先攻○")
        switch12=False
        ButtonAction()
    else:
        pass
def ButtonAction13():
    global TRUN
    global text13
    global switch13
    if switch13==True:
        if TRUN==0:
            Button13.config(text="〇",fg="red")
            ManageList[0][2]=1
            MainWin.title("○✕ゲーム 現在：後攻✕")
        if TRUN==1:
            Button13.config(text="✕",fg="blue")
            ManageList[0][2]=-1
            MainWin.title("○✕ゲーム 現在：先攻○")
        switch13=False
        ButtonAction()
    else:
        pass
def ButtonAction21():
    global TRUN
    global text21
    global switch21
    if switch21==True:
        if TRUN==0:
            Button21.config(text="〇",fg="red")
            ManageList[1][0]=1
            MainWin.title("○✕ゲーム 現在：後攻✕")
        if TRUN==1:
            Button21.config(text="✕",fg="blue")
            ManageList[1][0]=-1
            MainWin.title("○✕ゲーム 現在：先攻○")
        switch21=False
        ButtonAction()
    else:
        pass
def ButtonAction22():
    global TRUN
    global text22
    global switch22
    if switch22==True:
        if TRUN==0:
            Button22.config(text="〇",fg="red")
            ManageList[1][1]=1
            MainWin.title("○✕ゲーム 現在：後攻✕")
        if TRUN==1:
            Button22.config(text="✕",fg="blue")
            ManageList[1][1]=-1
            MainWin.title("○✕ゲーム 現在：先攻○")
        switch22=False
        ButtonAction()
    else:
        pass
def ButtonAction23():
    global TRUN
    global text23
    global switch23
    if switch23==True:
        if TRUN==0:
            Button23.config(text="〇",fg="red")
            ManageList[1][2]=1
            MainWin.title("○✕ゲーム 現在：後攻✕")
        if TRUN==1:
            Button23.config(text="✕",fg="blue")
            ManageList[1][2]=-1
            MainWin.title("○✕ゲーム 現在：先攻○")
        switch23=False
        ButtonAction()
    else:
        pass
def ButtonAction31():
    global TRUN
    global text31
    global switch31
    if switch31==True:
        if TRUN==0:
            Button31.config(text="〇",fg="red")
            ManageList[2][0]=1
            MainWin.title("○✕ゲーム 現在：後攻✕")
        if TRUN==1:
            Button31.config(text="✕",fg="blue")
            ManageList[2][0]=-1
            MainWin.title("○✕ゲーム 現在：先攻○")
        switch31=False
        ButtonAction()
    else:
        pass
def ButtonAction32():
    global TRUN
    global text32
    global switch32
    if switch32==True:
        if TRUN==0:
            Button32.config(text="〇",fg="red")
            ManageList[2][1]=1
            MainWin.title("○✕ゲーム 現在：後攻✕")
        if TRUN==1:
            Button32.config(text="✕",fg="blue")
            ManageList[2][1]=-1
            MainWin.title("○✕ゲーム 現在：先攻○")
        switch32=False
        ButtonAction()
    else:
        pass
def ButtonAction33():
    global TRUN
    global text33
    global switch33
    if switch33==True:
        if TRUN==0:
            Button33.config(text="〇",fg="red")
            ManageList[2][2]=1
            MainWin.title("○✕ゲーム 現在：後攻✕")
        if TRUN==1:
            Button33.config(text="✕",fg="blue")
            ManageList[2][2]=-1
            MainWin.title("○✕ゲーム 現在：先攻○")
        switch33=False
        ButtonAction()
    else:
        pass
def resetCOM():
    global TRUN,ManageList
    global switch11, switch12, switch13, switch21, switch22, switch23, switch31, switch32, switch33, switchF
    MainWin.title("○✕ゲーム 現在：先攻○")
    TRUN = 0
    ManageList = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    # texts
    Button11.config(text="-")
    Button11.config(fg='black')
    Button11.config(bg="whitesmoke")
    Button12.config(text="-")
    Button12.config(fg='black')
    Button12.config(bg="whitesmoke")
    Button13.config(text="-")
    Button13.config(fg='black')
    Button13.config(bg="whitesmoke")
    Button21.config(text="-")
    Button21.config(fg='black')
    Button21.config(bg="whitesmoke")
    Button22.config(text="-")
    Button22.config(fg='black')
    Button22.config(bg="whitesmoke")
    Button23.config(text="-")
    Button23.config(fg='black')
    Button23.config(bg="whitesmoke")
    Button31.config(text="-")
    Button31.config(fg='black')
    Button31.config(bg="whitesmoke")
    Button32.config(text="-")
    Button32.config(fg='black')
    Button32.config(bg="whitesmoke")
    Button33.config(text="-")
    Button33.config(fg='black')
    Button33.config(bg="whitesmoke")
    # switchs
    switch11 = True
    switch12 = True
    switch13 = True
    switch21 = True
    switch22 = True
    switch23 = True
    switch31 = True
    switch32 = True
    switch33 = True
    switchF = False
    LabelM.config(text="-")
    ButtonR.pack_forget()
    LabelM.pack_forget()
# print(ManageList)
   #print(sum1,sum2,sum3,sum4,sum5,sum6,sum7,sum8)
#frame
frame=tk.Frame(MainWin,relief='raised',height=410,width=510)
frame.pack()
#buttons
Button11=tk.Button(frame,text=text11,font=("",50),width=4,height=2,command=ButtonAction11)
Button12=tk.Button(frame,text=text12,font=("",50),width=4,height=2,command=ButtonAction12)
Button13=tk.Button(frame,text=text13,font=("",50),width=4,height=2,command=ButtonAction13)
Button21=tk.Button(frame,text=text21,font=("",50),width=4,height=2,command=ButtonAction21)
Button22=tk.Button(frame,text=text22,font=("",50),width=4,height=2,command=ButtonAction22)
Button23=tk.Button(frame,text=text23,font=("",50),width=4,height=2,command=ButtonAction23)
Button31=tk.Button(frame,text=text31,font=("",50),width=4,height=2,command=ButtonAction31)
Button32=tk.Button(frame,text=text32,font=("",50),width=4,height=2,command=ButtonAction32)
Button33=tk.Button(frame,text=text33,font=("",50),width=4,height=2,command=ButtonAction33)
ButtonR=tk.Button(MainWin,text="リセット",font=("", 50),command=resetCOM)
LabelM=tk.Label(MainWin,text="-",font=("",45))
#buttonset
Button11.grid(row=1,column=1)
Button12.grid(row=1,column=2)
Button13.grid(row=1,column=3)
Button21.grid(row=2,column=1)
Button22.grid(row=2,column=2)
Button23.grid(row=2,column=3)
Button31.grid(row=3,column=1)
Button32.grid(row=3,column=2)
Button33.grid(row=3,column=3)
#mainloop
MainWin.mainloop()
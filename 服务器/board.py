#!usr/bin/env python3.5
# -*- coding: utf-8 -*-

import tkinter
import datetime



def show():
    color={'1':'red','0':'white'}
    with open('wire_detected.txt','r')as f:
        wire_detected=f.read()

    with open('wire_status.txt','r')as f:
        wire_status=f.read()

    if wire_status!=wire_detected:

        with open('wire_status.txt','w')as f:
            f.write(wire_detected)
        
        for i in range(0,9):
            if i<5:
                tkinter.Label(root,bg=color[wire_detected[i]],width=4,height=2).place(x=38+i*52,y=120)
            else:
                tkinter.Label(root,bg=color[wire_detected[i]],width=4,height=2).place(x=38+(i-5)*52,y=205)
        for i in range(0,3):
            tkinter.Label(root,bg=color[wire_detected[i+9]],width=4,height=2).place(x=320,y=125+i*55)
    root.after(3000,show)     


with open('wire_status.txt','w')as f:
        f.write('0'*13)

root=tkinter.Tk()
root.geometry('480x320')
root.title("警戒系统")
root.resizable(0,0)
root.attributes('-topmost',1)
root.attributes('-fullscreen',1)


photo=tkinter.PhotoImage(file="背景.png")
img=tkinter.Label(root,image=photo)
img.place(x=0,y=0)


for i in range(0,9):
    if i<5:
        tkinter.Label(root,bg='white',width=4,height=2).place(x=38+i*52,y=120)
    else:
        tkinter.Label(root,bg='white',width=4,height=2).place(x=38+(i-5)*52,y=205)
        
for i in range(0,3):
    tkinter.Label(root,bg='white',width=4,height=2).place(x=320,y=125+i*55)
    


show()
root.update_idletasks()
root.mainloop()




















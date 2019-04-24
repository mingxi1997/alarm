#!usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
import socket
import time
from PIL import Image, ImageTk  
 
addr_order=['192.168.1.201','192.168.1.202','192.168.1.203','192.168.1.204','192.168.1.205','192.168.1.206','192.168.1.207','192.168.1.208','192.168.1.209']
addr_listen=['192.168.1.211','192.168.1.212','192.168.1.213']
commandbook={1000:'201',100:'202',10:'203',1100:'200',1010:'111',1001:'111',110:'301',101:'302',11:'111',1110:'101',1101:'102',1011:'103',1111:'100',1:'000',0:'000'}
alarmbook={'0000':'安全','0001':'警报1','0010':'警报2','0100':'警报3','1000':'警报4'}


def receive_case(case):
    with open(str(case)+'.txt','w') as f:
        f.write('1')

def solve_case(case):
    with open(str(case)+'.txt','w') as f:
        f.write('0')
def get_case(case):
    with open(str(case)+'.txt','r') as f:
        case=f.read()
    return case
        
       
    






def music_play(music):
     with open('music_play.txt','a')as f:
         f.write('\n'+music)



def safe_windows():
    Label(root,width=45,height=45,image=photo_white).place(x=1310,y=640)
    Label(root,width=45,height=45,image=photo_white).place(x=1310,y=640+70)
    Label(root,width=45,height=45,image=photo_white).place(x=1310,y=640+2*70)
            
    Label(root,width=30,height=2,text='当前 安全',font=("黑体", "12") ,bg='white').place(x=1500,y=650)
    Label(root,width=30,height=2,text='当前 安全',font=("黑体", "12") ,bg='white').place(x=1500,y=650+70)
    Label(root,width=30,height=2,text='当前 安全',font=("黑体", "12") ,bg='white').place(x=1500,y=650+2*70)

def up_windows():

    with open('alarm_listen.txt','r')as f:
        alert_code=eval(f.read())
    if get_case('alm_case')!=str(int(alert_code[0])+int(alert_code[1])+int(alert_code[2])):
        
        with open('alm_case.txt','w')as f:
            f.write(str(int(alert_code[0])+int(alert_code[1])+int(alert_code[2])))
        if int(alert_code[0])+int(alert_code[1])+int(alert_code[2])>0:
            
           
            
            with open('music_circle.txt','w')as f:
                f.write('1')

              

            for i in range(3):
                if int(alert_code[i])>0:   
                    Label(root,width=45,height=45,image=photo_red).place(x=1310,y=640+i*70)
                    try:
                        alarm_show=alarmbook[alert_code[i]]
                    except KeyError:
                        alarm_show='未知警报'
                    Label(root,width=30,height=2,text='警报 :'+alarm_show,font=("黑体", "12"),bg='red').place(x=1500,y=650+i*70)
                
            
    
            
        else:
            safe_windows()
            with open('music_circle.txt','w')as f:
                f.write('0')

    root.after(3000,up_windows)

    

    

         
def clear_all():
    for addr in addr_listen:
        feedback,error=send_signal(addr,'all00000000')
        
def get_status():
    with open('status.txt','r')as f:
        status=eval(f.read())
    return status
def save_status(status):
    with open('status.txt','w')as f:
        f.write(str(status))
        
        
def get_command():
    with open('command.txt','r')as f:
        command=eval(f.read())
    return command
def save_command(command):
    with open('command.txt','w')as f:
        f.write(str(command))
        
def command_standardize(command):
    stringcode='all'
    for i in range(1,9):
            stringcode+=str(command[i])
    return stringcode




def send_signal(addr,command):
    try:
        con=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        con.settimeout(1)
        con.sendto(command.encode("utf8"),(addr,5000))
        d1,addr_rev=con.recvfrom(1024)
        feedback='all'+d1.decode("utf8")[5:]
        error=0
    except socket.timeout:
        feedback='all00000000'
        error=1
    except:
        feedback='all00000000'
        error=1
    return feedback,error

 
 
def status_show():
    
    if get_case('case')=='1':
        solve_case('case')
        status=get_status()
 

        for keys,values in status.items():
                i=int(keys[-1])-1
                if values[-1]==1:
                    Label(width=10,height=2,bg='black',font=("Segoe UI Black", "12")).place(x=155+i*116,y=900)
                else:
                    try:
                        L=commandbook[int(values[0][3:7])]
                    except KeyError:
                        L='错误代号'
                    Label(width=10,height=2,text=L,font=("Segoe UI Black", "12")).place(x=155+i*116,y=900)
              
        
    root.after(3000,status_show)




def select_add():
    desks=[]
    if j1.get()==1:
        desks.append(addr_order[0])
    if j2.get()==1:
        desks.append(addr_order[1])
    if j3.get()==1:
        desks.append(addr_order[2])
    if j4.get()==1:
        desks.append(addr_order[3])
    if e1.get()==1:
        desks.append(addr_order[4])
    if e2.get()==1:
        desks.append(addr_order[5])
    if e3.get()==1:
        desks.append(addr_order[6])
    if e4.get()==1:
        desks.append(addr_order[7])
    if e5.get()==1:
        desks.append(addr_order[8])
   
    return desks

def open1():

    command=get_command()
    command[1]=int(not command[1])
    save_command(command)
    if command[1]==1: 
        c1['image']=photo1_d  
    else:
        c1['image']=photo1
       
        
        
                
    


   
    
    
def open2():
    
    command=get_command()
    command[2]=int(not command[2])
    
    save_command(command)
    if command[2]==1: 
        c2['image']=photo2_d  
    else:
        c2['image']=photo2
    
   


   
def open3():
    command=get_command()
    command[3]=int(not command[3])
    save_command(command)
    if command[3]==1: 
        c3['image']=photo3_d  
    else:
        c3['image']=photo3
    
   




def open4():
    command=get_command()
    command[4]=int(not command[4])
    save_command(command)
    if command[4]==1: 
        c4['image']=photo4_d  
    else:
        c4['image']=photo4
    
    
    


        
def send_all():
    receive_case('case')
    command=get_command()
    code=''
    for i in range(1,5):
        code+=str(command[i])
    code=int(code)
    
    get_case('case')
    try:
        
        print(commandbook[code])
        
        for k in commandbook.values():
            if commandbook[code]==k and commandbook[code]!='111':
                music_play('alert.mp3'+'\n'+commandbook[code]+'.mp3')
            elif commandbook[code]==k and commandbook[code]=='111':
                music_play('alert.mp3')

                
                
        
        for i in range(5,9):
            command[i]=command[i-4]
        save_command(command)
        
        
        addrs=select_add()
        command_s=command_standardize(command)
        
        for addr in addrs:
            feedback,error=send_signal(addr,command_s)
            status=get_status()
            status[addr]=[feedback,error]
            save_status(status)

        
            
        
        
    except KeyError:
        music_play('error.mp3')
        

        
    
    
    

  
solve_case('case')   
solve_case('alm_case')  
initial_command={1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
with open('command.txt','w')as f:
        f.write(str(initial_command))
status={}
for addr in addr_order:
        status[addr]=['all00000000',0]
with open('status.txt','w')as f:
    f.write(str(status))

root=Tk()
root.geometry('1920x1080')
root.title("警戒系统")
root.overrideredirect(True) 



photo=PhotoImage(file="背景.png")
img= Label(root,image=photo)
img.grid(row=0,column=0,rowspan=1000,columnspan=1000)





photo1=PhotoImage(file="红凸.png")
photo1_d=PhotoImage(file="红凹.png")
photo2=PhotoImage(file="黄凸.png")
photo2_d=PhotoImage(file="黄凹.png")
photo3=PhotoImage(file="蓝凸.png")
photo3_d=PhotoImage(file="蓝凹.png")
photo4=PhotoImage(file="绿凸.png")
photo4_d=PhotoImage(file="绿凹.png")
photo5=PhotoImage(file="发.png")

photo_affirm=PhotoImage(file="确认警报按钮.png")

photo_red=PhotoImage(file="red.png")

photo_white=PhotoImage(file="white.png")

c1=Button(root,relief="solid", bd=0)
c1['image']=photo1
c1['command']=open1
c1.place(x=200,y=260)

c2=Button(root,relief="sunken", bd=0)
c2['image']=photo2
c2['command']=open2
c2.place(x=500,y=260)

c3=Button(root,relief="sunken", bd=0)
c3['image']=photo3
c3['command']=open3
c3.place(x=800,y=260)

c4=Button(root,relief="sunken", bd=0)
c4['image']=photo4
c4['command']=open4
c4.place(x=1100,y=260)

c5=Button(root, relief="ridge", bd=40)
c5['image']=photo5
c5['command']=send_all
c5.place(x=1480,y=230)







c7=Button(root,image=photo_affirm,relief="raised", bd=10)
c7['command']=clear_all
c7.place(x=1380,y=870)


j1=IntVar()
check1=Checkbutton(root,width=1,height=1,pady=3,bg='green',activebackground='yellow',variable=j1)
check1.select()
check1.place(x=185,y=630)

j2=IntVar()
check2=Checkbutton(root,width=1,height=1,pady=3,bg='green',activebackground='yellow',variable=j2)
check2.select()
check2.place(x=185+116,y=630)

j3=IntVar()
check3=Checkbutton(root,width=1,height=1,pady=3,bg='green',activebackground='yellow',variable=j3)
check3.select()
check3.place(x=185+2*116,y=630)

j4=IntVar()
check4=Checkbutton(root,width=1,height=1,pady=3,bg='green',activebackground='yellow',variable=j4)
check4.select()
check4.place(x=185+3*116,y=630)

e1=IntVar()
check5=Checkbutton(root,width=1,height=1,pady=3,bg='green',activebackground='yellow',variable=e1)
check5.select()
check5.place(x=185+4*116,y=630)

e2=IntVar()
check6=Checkbutton(root,width=1,height=1,pady=3,bg='green',activebackground='yellow',variable=e2)
check6.select()
check6.place(x=185+5*116,y=630)

e3=IntVar()
check7=Checkbutton(root,width=1,height=1,pady=3,bg='green',activebackground='yellow',variable=e3)
check7.select()
check7.place(x=185+6*116,y=630)

e4=IntVar()
check8=Checkbutton(root,width=1,height=1,pady=3,bg='green',activebackground='yellow',variable=e4)
check8.select()
check8.place(x=185+7*116,y=630)

e5=IntVar()
check9=Checkbutton(root,width=1,height=1,pady=3,bg='green',activebackground='yellow',variable=e5)
check9.select()
check9.place(x=185+8*116,y=630)


safe_windows()
up_windows()

status_show()



root.update_idletasks()
root.mainloop()






















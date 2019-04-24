#!usr/bin/env python3.5
# -*- coding: utf-8 -*-


import datetime
import socket
import time
import subprocess
from playsound import playsound


addr_listen=['192.168.1.211','192.168.1.222','192.168.1.223']


now_time=str(datetime.datetime.now())[:-7]

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
        playsound('reboot_error.mp3')
    return feedback,error
        

def listen(addr_listen):
    state=[]
    command='read'
    for addr in addr_listen:
        feedback,error=send_signal(addr,command)
        state.append(feedback)
    return state


def get_alarm(state):
    n_state=[s[7:] for s in state]
    return n_state
        


    

def send_record(state):
    with open('alarm_listen.txt','w')as f:
                f.write(str(state))

def get_sum(alarm):
    sum_alarm=0
    for al in alarm:
        sum_alarm+=int(al)
    return sum_alarm


        
def read_timer():
    with open('timer.txt','r')as f:
        timer=int(f.read())
    return timer
def save_timer(timer):
    with open('timer.txt','w')as f:
        f.write(str(timer))
    

initial_alarm=['0000', '0000', '0000', '0000']
timer=0
save_timer(timer)
         
while True:
    time.sleep(2)

    timer=read_timer()
    if timer>20:
        timer=0
        save_timer(timer)
    
    
    state=listen(addr_listen)
    alarm=get_alarm(state)
    if alarm!=initial_alarm:
        initial_alarm=alarm
        send_record(alarm)#上交服务器状态

           

    
    timer+=1
    save_timer(timer)
            

            

        
            

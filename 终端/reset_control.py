#!usr/bin/env python3.5
# -*- coding: utf-8 -*-

import os
import datetime
import time


def read_timer():
    with open('timer.txt','r')as f:
        timer=int(f.read())
    return timer
def save_timer(timer):
    with open('timer.txt','w')as f:
        f.write(str(timer))
    
while True:


    timer=read_timer()
    timer+=1
    save_timer(timer)
    
    
    if timer>25:
        os.system('reboot')
    now_time=str(datetime.datetime.now())[11:-7]
    if int(now_time.replace(':',''))>120000 and int(now_time.replace(':',''))<120100:
        os.system('reboot')
    
    time.sleep(10)

        
            

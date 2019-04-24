#!usr/bin/env python3.5
# -*- coding: utf-8 -*-

import os
import datetime
import time


while True:


    now_time=str(datetime.datetime.now())[11:-7]
    if int(now_time.replace(':',''))>120000 and int(now_time.replace(':',''))<120100:
        os.system('reboot')
    
    time.sleep(30)

        
            

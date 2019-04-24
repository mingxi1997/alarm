#!usr/bin/env python3.5
# -*- coding: utf-8 -*-



import socket
import time
import subprocess

def playsound(path):
    subprocess.Popen(['mpg123', '-q', path]).wait()

all_addrs=(['192.168.1.201','192.168.1.202','192.168.1.203','192.168.1.204','192.168.1.205','192.168.1.206',
            '192.168.1.207','192.168.1.208','192.168.1.209','192.168.1.211','192.168.1.212','192.168.1.213'])

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
        
def test_connection():
    status=[]
    connection=''
    for addr in all_addrs:
        feedback,error=send_signal(addr,'read')
        status.append(feedback)
        connection+=str(error)
    return status,connection




while True:
    time.sleep(3)    
    status,connection=test_connection()
    with open('wire_detected.txt','w')as f:
        f.write(connection)
    
    if int(connection)!=0:
        playsound('wire_error.mp3')
        playsound('wire_error2.mp3')

            

        
            

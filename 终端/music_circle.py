

import time
import subprocess

def playsound(path):
    subprocess.Popen(['mpg123', '-q', path]).wait()
def music_play(music):
     with open('music_play.txt','a')as f:
         f.write('\n'+music)
while True:
    with open('music_circle.txt','r')as f:
                circle=f.read()
    if circle=='1':
        playsound('receive_alarm.mp3')
        playsound('alarm.mp3')
    time.sleep(3)

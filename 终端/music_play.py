
import time
import subprocess

def playsound(path):
    subprocess.Popen(['mpg123', '-q', path]).wait()


with open('music_play.txt','w')as f:
    f.write('rest')
    
while True:
    time.sleep(2)
    with open('music_play.txt','r')as f:
        music=f.read()
    if music=='rest':
        pass
    else:
        music_lists=music.split('\n')
        for mu in music_lists:
            if mu=='rest' or mu=='':
                pass
            else:
                playsound(mu)

    with open('music_play.txt','w')as f:
            f.write('rest')
        
    






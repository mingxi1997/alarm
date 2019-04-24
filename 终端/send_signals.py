import time
def music_play(music):
     with open('music_play.txt','a')as f:
         f.write('\n'+music)


music_play('101.mp3')
time.sleep(3)
music_play('201.mp3')

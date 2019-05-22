from multiprocessing import Process
import subprocess
import time

DEBUG = True

def play_alarm():
    bashCommand = "omxplayer --loop sound.mp3"
    bash_sub_process = subprocess.run(bashCommand, shell = True)


kill_alarm = False
play_process = Process(target = play_alarm)
play_process.daemon = True
play_process.start()

if DEBUG:
    print(play_process.pid)

time.sleep(5)

#while not(kill_alarm):
#    c = "1"
    #wait for rfid check

play_process.terminate()

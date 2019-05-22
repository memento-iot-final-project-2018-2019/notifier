from multiprocessing import Process
import subprocess
import time

DEBUG = True

def play_alarm():
    bashCommand = "omxplayer --loop sound.mp3"
    omx_sub_process = subprocess.run(bashCommand, shell = True)
    time.sleep(5)
    bashCommand = "pkill -SIGINT omxplayer.bin"
    omx_terminator = subprocess.Popen(bashCommand, shell = True)
    omx_terminator.wait()


#kill_alarm = False
# This will be called when the proximity sensor detects 
play_process = Process(target = play_alarm)
play_process.daemon = True
play_process.start()

if DEBUG:
    print(play_process.pid)

time.sleep(5)

#while not(kill_alarm):
#    c = "1"
    #wait for rfid check

#play_process.terminate()

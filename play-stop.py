from multiprocessing import Process
import subprocess

DEBUG = True

def play_alarm():
    bashCommand = "sh play_alarm.sh"
    bash_sub_process = subprocess.run(bashCommand, shell = True)


kill_alarm = False
play_process = Process(target = play_alarm)
play_process.daemon = True
play_process.start()

if DEBUG:
    print(play_process.pid)

while not(kill_alarm):
    c = "1"
    #wait for rfid check

play_process.terminate()

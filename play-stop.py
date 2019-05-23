import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

from omxplayer.player import OMXPlayer
from pathlib import Path
import time

#########################################
### REMEMBER! WRITE THE TAG ONLY ONCE ###
#########################################
INIT_TAG = False

reader = SimpleMFRC522()

if INIT_TAG:
    try:
        print('before write')
        reader.write('k')
        print('after write')
    finally:
        GPIO.cleanup()

AUDIO_PATH = Path("sound.m4a")

kill_alert = False

door_open = True

player = OMXPlayer(AUDIO_PATH, args=['--no-osd', '--no-keys', '--loop'])
player.pause()

while True:
    kill_alert = False
    #####################
    ##CHECK PROX SENSORS#
    #####################
    if door_open and kill_alert == False:
        print("Starting alert")
        player.play()
        try:
            kill_alert = reader.read()
            print('read tag')
        finally:
            GPIO.cleanup()
        player.pause()
        time.sleep(60)

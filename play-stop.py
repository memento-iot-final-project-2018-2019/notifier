from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep

AUDIO_PATH = Path("sound.mp3")

player = OMXPlayer(AUDIO_PATH, args=['--no-osd', '--no-keys', '--loop'])

player.play()

# WAIT For RFID TAG TO KILL ALARM
sleep(5)
player.quit()

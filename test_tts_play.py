import winsound
import time

winsound.PlaySound('tts.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)

time.sleep(10)
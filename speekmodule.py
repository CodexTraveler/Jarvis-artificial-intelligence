from gtts import gTTS
import random
import os

def speek(rand,n,mixer):
    tts = gTTS(text=random.choice(rand), lang='en')                 
    tts.save('jarvis'+str(n)+'.mp3')
    mixer.init()
    mixer.music.load('jarvis'+str(n)+'.mp3')
    mixer.music.play()

def wifi():
    REMOTE_SERVER = "www.google.com"
    def is_connected():
        try:
            host = socket.gethostbyname(REMOTE_SERVER)
            s = socket.create_connection((host, 80), 2)
            return True
        except:
            pass
        return False

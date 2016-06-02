#!/usr/bin/env python
#
# Copyright 2016 Jarvis
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from gtts import gTTS
import pyaudio
import speech_recognition as sr
from pygame import mixer
import os
import random
import socket
import webbrowser
import subprocess
import glob
from time import localtime, strftime
doss = os.getcwd()
i=0
n=0

INFO = '''
        +=======================================+
        |.....JARVISE VIRTUAL INTELLIGENCE......|
        +---------------------------------------+
        |#Author: Valentin Genard               |
        |#Date: 01/06/2016                      |
        |#Changing the Description of this tool |
        | Won't made you the coder              |
        |#I don't take responsability for       |
        | problems of any kind                  |
        +---------------------------------------+
        |.....JARVISE VIRTUAL INTELLIGENCE......|
        +=======================================+
        |              OPTIONS:                 |
        |#hello/hi     #goodbye    #sleep mode  |
        |#your name    #jarvis     #what time   |
        |#asite.com    #next music #music       |
        |#pause music  #wifi       #thank you   |
        |#start/stop someapp                    |
        |#pip install/desinstall anapp          |
        |#googlemaps tanyplace                  |
        +=======================================+
        '''

# JARVIS'S EARS========================================================================================================== SENSITIVE BRAIN
                                            #------------- obtain audio
while (i<1):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.adjust_for_ambient_noise(source)
        n=(n+1)

        print(INFO)
        print("Say something!")
        audio = r.listen(source)

                            #------------- interprete audio (Google Speech Recognition)
    try:
        s = (r.recognize_google(audio))
        message = (s.lower())
        print (message)


# POLITE JARVIS ============================================================================================================= BRAIN 1
    
        if ('goodbye') in message:                          
            rand = ['Goodbye Sir', 'Jarvis powering off in 3, 2, 1, 0']
            tts = gTTS(text=random.choice(rand), lang='en')                #------------>       STOP JARVIS
            tts.save('jarvis'+str(n)+'.mp3')
            mixer.init()
            mixer.music.load('jarvis'+str(n)+'.mp3')
            mixer.music.play()
            break
            
        if ('hello') in message or ('hi') in message:
            rand = ['Wellcome to Jarvis virtual intelligence project. At your service sir.']
            tts = gTTS(text=random.choice(rand), lang='en')                #------------>          HELLO
            tts.save('jarvis'+str(n)+'.mp3')
            mixer.init()
            mixer.music.load('jarvis'+str(n)+'.mp3')
            mixer.music.play()

        if ('thanks') in message or ('tanks') in message or ('thank you') in message:
            rand = ['You are wellcome', 'no problem']
            tts = gTTS(text=random.choice(rand), lang='en')                #------------>      You're wellcome
            tts.save('jarvis'+str(n)+'.mp3')
            mixer.init()
            mixer.music.load('jarvis'+str(n)+'.mp3')
            mixer.music.play()

        if message == ('jarvis'):
            rand = ['Yes Sir?', 'What can I doo for you sir?']
            tts = gTTS(text=random.choice(rand), lang='en')                 #----------->   RESPOND WHEN CALLED
            tts.save('jarvis'+str(n)+'.mp3')
            mixer.init()
            mixer.music.load('jarvis'+str(n)+'.mp3')
            mixer.music.play()

        if  ('how are you') in message or ('and you') in message or ('are you okay') in message:
            rand = ['Fine thank you']
            tts = gTTS(text=random.choice(rand), lang='en')                 #------------->    HOW IS JARVIS
            tts.save('jarvis'+str(n)+'.mp3')
            mixer.init()
            mixer.music.load('jarvis'+str(n)+'.mp3')
            mixer.music.play()

        if  ('*') in message:
            rand = ['Be polite please']
            tts = gTTS(text=random.choice(rand), lang='en')                 #------------->  BE POLITE WITH JARVIS
            tts.save('jarvis'+str(n)+'.mp3')
            mixer.init()
            mixer.music.load('jarvis'+str(n)+'.mp3')
            mixer.music.play()

        if ('your name') in message:
            rand = ['My name is Jarvis, at your service sir']
            tts = gTTS(text=random.choice(rand), lang='en')                 #------------->    JARVIS'S NAME
            tts.save('jarvis'+str(n)+'.mp3')
            mixer.init()
            mixer.music.load('jarvis'+str(n)+'.mp3')
            mixer.music.play()

# USEFUL JARVIS ============================================================================================================= BRAIN 2

        if ('wi-fi') in message:  
            REMOTE_SERVER = "www.google.com"
            def is_connected():
              try:
                host = socket.gethostbyname(REMOTE_SERVER)
                s = socket.create_connection((host, 80), 2)
                return True
              except:
                 pass
              return False
            tts = gTTS('we are connected', lang='en')                      #----------->   Say if wifi is connected
            tts.save('jarvis'+str(n)+'.mp3')
            mixer.init()
            mixer.music.load('jarvis'+str(n)+'.mp3')
            mixer.music.play()

        if ('.com') in message :
            rand = ['Opening' + message]
            tts = gTTS(text=random.choice(rand), lang='en')                #------------->     Searchanysite.com
            tts.save('jarvis'+str(n)+'.mp3')
            mixer.init()
            mixer.music.load('jarvis'+str(n)+'.mp3')
            mixer.music.play()
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            webbrowser.get(Chrome).open('http://www.'+message)

        if ('google maps') in message:
            query = message
            stopwords = ['google', 'maps']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            rand = [result+'on google maps']
            tts = gTTS(text=random.choice(rand), lang='en')                #------------->     google maps anyplace
            tts.save('jarvis'+str(n)+'.mp3')
            mixer.init()
            mixer.music.load('jarvis'+str(n)+'.mp3')
            mixer.music.play()
            webbrowser.get(Chrome).open("https://www.google.be/maps/place/"+result+"/")
            
        if ('start') in message:
            query = message
            stopwords = ['start']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            os.system('start ' + result)
            tts = gTTS(text='starting'+result, lang='en')                     #------------->     START APROGRAM
            tts.save('jarvis'+str(n)+'.mp3')
            mixer.init()
            mixer.music.load('jarvis'+str(n)+'.mp3')
            mixer.music.play()

        if ('stop') in message:
            query = message
            stopwords = ['stop']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            os.system('taskkill /im ' + result + '.exe /f')
            tts = gTTS(text='stopping'+result, lang='en')                     #------------->      STOPAPROGRAM
            tts.save('jarvis'+str(n)+'.mp3')
            mixer.init()
            mixer.music.load('jarvis'+str(n)+'.mp3')
            mixer.music.play()

        if ('install') in message:
            query = message
            stopwords = ['install']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            tts = gTTS(text='trying to install '+result, lang='en')        #---------------->   PIP INSTALL APROGRAM
            tts.save('jarvis'+str(n)+'.mp3')
            mixer.init()
            mixer.music.load('jarvis'+str(n)+'.mp3')
            mixer.music.play()
            os.system('python -m pip install ' + result)

        if ('desinstall') in message:
            query = message
            stopwords = ['desinstall']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            tts = gTTS(text='trying to desinstall '+result, lang='en')      #----------------> PIP DESINSTALL APROGRAM
            tts.save('jarvis'+str(n)+'.mp3')
            mixer.init()
            mixer.music.load('jarvis'+str(n)+'.mp3')
            mixer.music.play()
            os.system('python -m pip desinstall ' + result)

        if ('sleep mode') in message:
            query = message
            stopwords = ['desinstall']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            tts = gTTS(text='trying to desinstall '+result, lang='en')      #---------------->     SLEEP COMPUTER
            tts.save('jarvis'+str(n)+'.mp3')
            mixer.init()
            mixer.music.load('jarvis'+str(n)+'.mp3')
            mixer.music.play()
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

        if ('music') in message:
            mus = glob.glob(doss + "\\music" + "\\*.mp3") #specify music folder
            text=random.choice(mus)
            tts = gTTS(text='start playing', lang='en')                     #--------------->       PLAY MUSIC
            tts.save('jarvis'+str(n)+'.mp3')
            mixer.init()
            mixer.music.load(text)
            mixer.music.play()
            if ('pause') in message:
                mixer.music.pause()

        if ('what time') in message:
            tim = strftime("%X", localtime())
            tts = gTTS(text=tim, lang='en')                                  #------------->        SAY TIME
            tts.save('jarvis'+str(n)+'.mp3')
            mixer.init()
            mixer.music.load('jarvis'+str(n)+'.mp3')
            mixer.music.play()

    # exceptions
    except sr.UnknownValueError:
        print("$could not understand audio")
    except sr.RequestError as e:
        print("Could not request results$; {0}".format(e))

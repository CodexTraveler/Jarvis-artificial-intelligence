#!/usr/bin/env python
#
# Copyright 2010 Facebook
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
import speekmodule

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
        |#pip install/uninstall anapp          |
        |#googlemaps tanyplace                  |
        +=======================================+
        '''
print(INFO)
# JARVIS'S EARS========================================================================================================== SENSITIVE BRAIN
                                                   # obtain audio
while (i<1):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.adjust_for_ambient_noise(source)
        n=(n+1)     
        print("Say something!")
        audio = r.listen(source)
                                                   # interprete audio (Google Speech Recognition)
    try:
        s = (r.recognize_google(audio))
        message = (s.lower())
        print (message)


# POLITE JARVIS ============================================================================================================= BRAIN 1
    
        if ('goodbye') in message:                          
            rand = ['Goodbye Sir', 'Jarvis powering off in 3, 2, 1, 0']
            speekmodule.speek(rand,n,mixer)
            break
            
        if ('hello') in message or ('hi') in message:
            rand = ['Wellcome to Jarvis virtual intelligence project. At your service sir.']
            speekmodule.speek(rand,n,mixer)

        if ('thanks') in message or ('tanks') in message or ('thank you') in message:
            rand = ['You are wellcome', 'no problem']
            speekmodule.speek(rand,n,mixer)

        if message == ('jarvis'):
            rand = ['Yes Sir?', 'What can I doo for you sir?']
            speekmodule.speek(rand,n,mixer)

        if  ('how are you') in message or ('and you') in message or ('are you okay') in message:
            rand = ['Fine thank you']
            speekmodule.speek(rand,n,mixer)

        if  ('*') in message:
            rand = ['Be polite please']
            speekmodule.speek(rand,n,mixer)

        if ('your name') in message:
            rand = ['My name is Jarvis, at your service sir']
            speekmodule.speek(rand,n,mixer)

# USEFUL JARVIS ============================================================================================================= BRAIN 2

        if ('wi-fi') in message:  
            REMOTE_SERVER = "www.google.com"
            speekmodule.wifi()
            rand = ['We are connected']
            speekmodule.speek(rand,n,mixer)

        if ('.com') in message :
            rand = ['Opening' + message]         
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            speekmodule.speek(rand,n,mixer)
            webbrowser.get(Chrome).open('http://www.'+message)
            print ('')
            

        if ('google maps') in message:
            query = message
            stopwords = ['google', 'maps']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            webbrowser.get(Chrome).open("https://www.google.be/maps/place/"+result+"/")
            rand = [result+'on google maps']
            speekmodule.speek(rand,n,mixer)

        if message != ('start music') and ('start') in message:   
            query = message
            stopwords = ['start']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            os.system('start ' + result)
            rand = [('starting '+result)]
            speekmodule.speek(rand,n,mixer)

        if message != ('stop music') and ('stop') in message:
            query = message
            stopwords = ['stop']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            os.system('taskkill /im ' + result + '.exe /f')
            rand = [('stopping '+result)]
            speekmodule.speek(rand,n,mixer)

        if ('install') in message:
            query = message
            stopwords = ['install']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            rand = [('installing '+result)]
            speekmodule.speek(rand,n,mixer)
            os.system('python -m pip install ' + result)


        if ('sleep mode') in message:
            rand = ['good night']
            speekmodule.speek(rand,n,mixer)
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

        if ('music') in message:
            mus = random.choice(glob.glob(doss + "\\music" + "\\*.mp3"))
            os.system('chown -R user-id:group-id mus')
            os.system('start ' + mus)
            rand = ['start playing']
            speekmodule.speek(rand,n,mixer)

        if ('what time') in message:
            tim = strftime("%X", localtime())
            rand = [tim]
            speekmodule.speek(rand,n,mixer)

    # exceptions
    except sr.UnknownValueError:
        print("$could not understand audio")
    except sr.RequestError as e:
        print("Could not request results$; {0}".format(e))

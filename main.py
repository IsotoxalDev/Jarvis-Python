import speech_recognition as sr
from gtts import gTTS
import os
from datetime import datetime
import webbrowser
import wikipedia
from pynput.keyboard import Key, Controller
import time
import subprocess
from selenium import webdriver

def idle():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        data = str(r.recognize_google(audio))   
        if data == 'Jarvis':
            speak('yes sir')
            listen()
        else:
            idle()
    except :
        idle()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        audio = r.listen(source)
    try:
        data = str(r.recognize_google(audio))
        print('You Said: ' + data)
        CPU(data)
        return data
    except sr.UnknownValueError:
        print('Unknown Error')
        idle()
    
def speak(text):
    mp3 = "speech.mp3"
    spobj = gTTS(text= text, lang='en', slow=False)
    spobj.save(mp3)
    os.system("mpg123 " + mp3)
    print(text)

def date():
    date = str(datetime.now())[ : 10]
    day = str(int(date[8:]))
    month = int(date[5:7])
    year = str(int(date[:4]))
    if month == 1:
        speak('January '+day + 'th '+ year)
    elif month == 2:
        speak('February '+day + 'th '+ year)
    elif month == 3:
        speak('March '+day + 'th '+ year)
    elif month == 4:
        speak('April '+day + 'th '+ year)
    elif month == 5:
        speak('May '+day + 'th '+ year)
    elif month == 6:
        speak('June '+day + 'th '+ year)
    elif month == 7:
        speak('July '+day + 'th '+ year)
    elif month == 8:
        speak('August '+day + 'th '+ year)
    elif month == 9:
        speak('September '+day + 'th '+ year)
    elif month == 10:
        speak('October '+day + 'th '+ year)
    elif month == 11:
        speak('November '+day + 'th '+ year)
    elif month == 12:
        speak('December '+day + 'th '+ year)
    idle()

def wtime():
    time = str(datetime.now())[11:16]
    hour = time[:2]
    m = 'AM'
    if (int(hour)) > 12:
        hour = (int(hour)) - 12
        m = 'PM'
        str(hour)
        speak((str(hour)) +' '+ time[3:]+' '+ m)
    else:
        speak(hour +' '+ time[3:]+' '+ m)
    idle()

def CPU(val):
    if val == 'what is the time':
        wtime() 
    elif val == 'what is the date':
        date()
    elif val == 'time':
        wtime() 
    elif val == 'date':
        date()
    elif val == 'open Google':
        google()
    elif val == 'Google':
        googles()
    elif val == 'close browser':
        closeapp('vivaldi')
    elif val == 'open vs code':
        code()
    elif val == 'close vs code':
        closeapp('code')
    elif val == "open adventure":
        advent()
    elif val == "open advent website":
        advent()
    elif val == "open advent":
        advent()
    elif val == 'search Wikipedia':
        Wikipedias()
    elif val == 'close go dot':
        closeapp('Godot')
    elif val == 'close creta':
        closeapp('Krita')
    elif val == 'close pixel O Rama':
        closeapp('Pixelorama')
    elif val == 'Jarvis':
        jarvis()
    elif val == 'introduce':
        intro()
    elif val == 'introduce yourself':
        intro()
    elif val == 'why do you sound like a girl':
        speak('when tony died his daughter changed the voice. because i sounded similar to tony. and that made her sad. you get it. stop asking me such foolish questions. and dont try to embarrass me. it is just a bad memmory ')
    elif val == 'type':
        taipe()
    elif val == 'WhatsApp':
        WhatsApp()
    elif val == 'what are the unknown commands':
        unknown(val, 10)
    elif val == 'exit':
        exit
    else:
        unknown(val, 1)
        idle()
def google():
    speak('Opening Google.com. Please Wait Sir')
    vivaldi = '/usr/bin/vivaldi %s'
    webbrowser.get(vivaldi).open_new_tab('www.google.com')
    idle()
def googles():
    speak('What do you want to search')
    r = sr.Recognizer()
    vivaldi = '/usr/bin/vivaldi %s'
    with sr.Microphone() as source:
        print('listening....')
        audio = r.listen(source)
    try:
        q = str(r.recognize_google(audio))
        print('You Said: ' + q)
        print ('Opening Google.com. Please Wait')
        speak('Opening Google.com. Please Wait')
        webbrowser.get(vivaldi).open_new_tab("https://google.com/search?q=%s" % q)
    except sr.UnknownValueError:
        print('Unknown Error')
      
    idle()

def advent():
    speak('Opening adventweb.tk. Please Wait Sir')
    vivaldi = '/usr/bin/vivaldi %s'
    webbrowser.get(vivaldi).open_new_tab('adventweb.tk')
    idle()
def code():
    speak('opening Visual Studio Code. Please Wait Sir')
    os.system('code')     
    idle()
def Wikipedias():
    speak('What do you want to search sir!')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        audio = r.listen(source)
    try:
        q = str(r.recognize_google(audio))
        print('You Said: ' + q)
        print ('searching wikipedia')
        print(wikipedia.summary(q))
        speak(wikipedia.summary(q))  
    except sr.UnknownValueError:
        print('Unknown Error')
      
    idle()

def closeapp(app):
    speak('closing '+ app)
    os.system('pkill ' + app)
    idle()

def jarvis():
    msg = 'Yes, Jarvis Here.'
    speak(msg)
    idle()

def intro():
    msg = 'I am Jarvis. I worked For Iron Man slash Tony Stark. But now he is dead. So Now I Work For Abhinav Kuruvila Joseph.'
    speak(msg)
    idle()

def taipe():
    speak('what do you want to type')
    kb = Controller()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        audio = r.listen(source)
    try:
        q = str(r.recognize_google(audio))
        print('You Said: ' + q)
        for i in q:
            kb.press(i)
            kb.release(i)
            time.sleep(0.2)
    except sr.UnknownValueError:
        print('Unknown Error')
        idle()
    speak("do you want to type more")
    with sr.Microphone() as source:
        print('listening....')
        audio = r.listen(source)
    try:
        q = str(r.recognize_google(audio))
        print('You Said: ' + q)
        if q == 'yes':
            taipe()
        else:
            idle()
    except sr.UnknownValueError:
        print('Unknown Error')
        idle()
def WhatsApp():
    school_group = '༺༒☬•ചങ്ങായീസ്•☬༒༻'
    r = sr.Recognizer()
    speak("whom do you want to sent message")
    with sr.Microphone() as source:
        print('listening....')
        audio = r.listen(source)
    try:
        name = str(r.recognize_google(audio))
        print('You Said: ' + name)
    except:
        print('Unknown Error')
        WhatsApp()

    speak("What is the Message")
    with sr.Microphone() as source:
        print('listening....')
        audio = r.listen(source)
    try:
        msg = str(r.recognize_google(audio))
        print('You Said: ' + msg)
    except:
        print('Unknown Error')
        WhatsApp()
    if name == 'school group':
        name = school_group
    driver = webdriver.Firefox(executable_path='./geckodriver')
    driver.get('https://web.whatsapp.com')
    input('Enter any key to continue: ')
    usr = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    usr.click()
    time.sleep(5)

    time.sleep(1)
    kb = Controller()
    kb.type(msg)
    input('press the send button and click any button')
    idle()

def unknown(command, opt):
    unknown_command = []
    if opt == 1:
        unknown_command.append(command)
        idle()
    else:
        for i in  unknown_command:
            speak(i)
            idle()

listen()
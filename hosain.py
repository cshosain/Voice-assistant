from email.mime import audio
from http import server
import smtplib
from tkinter.tix import NoteBook
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import subprocess

contats = {"hosain":"hosainandh@gmail.com","ahad":"ahadulalam@gmail.com"}

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am your assistant Sir.")

def takeCommand():
    #it takes microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #jotokhon por listen kora off korbe
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='English')
        print(f"User said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "none"
    return query
    

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("mahimhosain102@gmail.com","Mahim&Password1")
    server.sendmail("mahimhosain102@gmail.com",to,content)
    server.close()

def askExit():
    speak("Do you wand to exit?")
    print("Send\nDo you want to exit? yes \\ no?")
    query = takeCommand().lower()
    if 'yes' in query:
        exit()
        
        


if __name__=="__main__":
    wishMe()
    while True:
    
        #lower for matching query because sometime recognized string is capiatal mixed
        speak("Please tell me how may I help you?")
        query = takeCommand().lower()

        # Login for execute task based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            #replacing query variable to blank oc clean
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            askExit()

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            askExit()

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            askExit()

        elif 'open google' in query:
            webbrowser.open("google.com")
            askExit()

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            askExit()

        elif 'play music' in query:
            music_dir = 'D:\\Music'
            # listdir list all song in the given(D:\\Music\\song1) directory
            songs = os.listdir(music_dir)
            #os.startfile open the file and gather all song of given directory and attach the song
            # here i can generate random number and put song arry index to play random song 
            os.startfile(os.path.join(music_dir, songs[0]))
            askExit()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            askExit()

        elif 'open code' in query:
            codePath = '"C:\\Users\\Hosain\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            # here for app os.startfile
            os.startfile(codePath)
            askExit()

        elif "calculator" in query:
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
            askExit()

        elif "notepad" in query:
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
            askExit()

        elif 'email to' in query:
            try:
                speak("What should I say?")
                to = contats["hosain"]
                content = takeCommand()
                sendEmail(to,content)
                speak("Email has been sent!")
                askExit() # ask to user wheather exit or not
                
            except Exception as e:
                print(e)
                speak("Sorry sir I am not avail to sent the email")

        else:
            speak("Sorry sir, I could no heared clearly.")
            askExit()
            speak("Or again")



from email.mime import audio
from tkinter.tix import NoteBook
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

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

    speak("I am Jarvis Sir. Please tell me how may I help you")

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

if __name__=="__main__":
    wishMe()
    while True:
    
        #lower for matching query because sometime recognized string is capiatal mixed
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

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'play music' in query:
            music_dir = 'D:\\Music'
            # listdir list all song in the given(D:\\Music\\song1) directory
            songs = os.listdir(music_dir)
            print(songs)
            #os.startfile open the file and gather all song of given directory and attach the song
            # here i can generate random number and put song arry index to play random song 
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = '"C:\\Users\\Hosain\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            # here for app os.startfile
            os.startfile(codePath)

            #next is comming soon



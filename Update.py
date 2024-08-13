import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import gmplot 
from os import startfile
import requests
from bs4 import BeautifulSoup
import pywhatkit
import pyautogui


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
     
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")   
    else:
        speak("Good Evening Sir!")  

    speak("I am Zippy. Please tell me how may I help you")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        
        print("Say that again please...")  
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play some song' in query:
            webbrowser.open("https://open.spotify.com//search/{song}")
        
        elif 'tell me a  time' in query or "wahts the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)    
            speak(f"Sir, the time is {strTime}")

        elif "date" in query or "current date" in query:
            date= datetime.datetime.now().strftime("%d / %m / %Y")
            print(date)
            speak("Today's date "+ date)

        elif "open facebook" in query:
            webbrowser.open("https://www.facebook.com/")

        elif "open twitter" in query:
            webbrowser.open("https://twitter.com/")
            
        elif "open instagram" in query:
            webbrowser.open("https://www.instagram.com/")

        elif "open linkedin" in query:
            webbrowser.open("https://www.linkedin.com/")
    
        elif "set an alarm" in query:
            print("input time example:- 10 and 10 and 10")
            speak("Set the time")
            a = input("Please tell the time :- ")
            alarm(a)
            speak("Done,sir")

        elif "temperature" in query:
            search = "temperature in mathura"
            url = f"https://www.google.com/search?q={search}"
            r  = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current{search} is {temp}")
 

        elif "news" in query or "headlines" in query:
            from NewsRead import latestnews
            latestnews()

        elif "calculate" in query:
            from calculatenumbers import WolfRamAlpha
            from calculatenumbers import Calc
            query = query.replace("calculate","")
            query = query.replace("Zippy","")
            Calc(query)     

        elif "introduction" in query or "tell me about yourself" in query:
            print("Sir my name is Zippy. I am Virtual Assistant made by python programming language. I do several things as you want to command")
            speak("Sir my name is Zippy. I am Virtual Assistant made by python programming language. I do several things as you want to command")


        



       
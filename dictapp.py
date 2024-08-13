import os 
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp = {"commandprompt":"cmd","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt"}
def openapp(query):
    speak("Launching, sir")
    keys = list(dictapp.keys())
    for app in keys:
        if app in query:
            os.system(f"start {dictapp[app]}")

def closeapp(query):
    speak("Closing,sir")
keys = list(dictapp.keys())
for app in keys:
    if app in query:
        os.system(f"taskkill /f /im {dictapp[app]}.exe")
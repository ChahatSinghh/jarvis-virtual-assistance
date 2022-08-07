#project started on 1 august 2022
import pyttsx3 #importing module
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5') #sapi5 is API by microsoft that provides voice
voices=engine.getProperty('voices')#to get one of the voice out of male or female
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("Hello sir or mam ,this is jarvis please tell me how may i help you?")

def takeCommand():

if __name__=="__main__":
    wishMe()
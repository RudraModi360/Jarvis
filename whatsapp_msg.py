import os
import pyautogui
from keyboard import write
from time import sleep
from keyboard import press
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print("User said: ",query)

    except Exception as e:
        print("Can't Reach At ,This Moment...")    
        print("Say that again please...")  
        return "None"
    return query
def WhatsappMsg(name,message):
    os.startfile("C:\\Users\\Rudra\\OneDrive\\Desktop\\WhatsApp - Shortcut.lnk")
    sleep(10)
    pyautogui.click(x=195,y=115)
    sleep(1)
    write(name)
    sleep(1)   
    pyautogui.click(x=188,y=249)
    sleep(1)
    pyautogui.click(x=915, y=952)
    sleep(1)
    write(message)
    sleep(5)
    T=TakeCommand()
    if T=="confirm":
        press("enter")
    else:
        quit()
def Whatsapp_VOICE_Call(name):
    os.startfile("C:\\Users\\Rudra\\OneDrive\\Desktop\\WhatsApp - Shortcut.lnk")
    sleep(5)
    pyautogui.click(x=195,y=115)
    sleep(1)
    write(name)
    sleep(1)   
    pyautogui.click(x=188,y=249)
    sleep(1)
    pyautogui.click(x=915, y=952)
    sleep(1)
    pyautogui.click(x=1198,y=63)
    sleep(1)
    press("enter")  
def Whatsapp_VIDEO_Call(name):
    os.startfile("C:\\Users\\Rudra\\OneDrive\\Desktop\\WhatsApp - Shortcut.lnk")
    sleep(10)
    pyautogui.click(x=195,y=115)
    sleep(1)
    write(name)
    sleep(1)   
    pyautogui.click(x=188,y=249)
    sleep(1)
    pyautogui.click(x=915, y=952)
    sleep(1)
    pyautogui.click(x=1658, y=105)
    sleep(1)
    speak("Do You Really Want Place The Video Call.....")
    press("enter")
            

    

while True:
    query=TakeCommand().lower()
    if "message"in query:
        query=query.replace("message","")
        name=query
        speak("Let Me Know The Message....")
        Message=TakeCommand()
        write(Message)
        WhatsappMsg( name,Message)
    elif "voice call" in query:
        query=query.replace("voice call","")
        name=query
        Whatsapp_VOICE_Call(name)
    elif "video call" in query:
        query=query.replace("video call","")
        name=query
        Whatsapp_VIDEO_Call(name)
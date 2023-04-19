import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os 
import pyautogui
from keyboard import write
from time import sleep
from keyboard import press
import pywhatkit
from pyjokes import get_joke
import python_weather
import asyncio


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 6:
        speak("Good Night ,BOSS!!")

    elif hour >= 6 and hour < 12:
        speak("Good Morning ,BOSS!!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon ,BOSS!!")

    elif hour >= 18 and hour <= 21:
        speak("Good Evening ,BOSS!!")

    speak("How May I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Jarvis Was Sleeping ,Yet")
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)

    except Exception as e:
        print("Can't Reach At ,This Moment...")
        print("Say that again please...")
        return "None"
    return query


def WhatsappMsg(name, message):
    speak("Opening What'sapp...")
    os.startfile(
        "C:\\Users\\Rudra\\OneDrive\\Desktop\\WhatsApp - Shortcut.lnk")
    sleep(10)
    pyautogui.click(x=195, y=115)
    sleep(1)
    speak("Making Search...")
    write(name)
    sleep(1)
    pyautogui.click(x=188, y=249)
    sleep(1)
    pyautogui.click(x=915, y=952)
    sleep(1)
    speak("Typing message")
    write(message)
    sleep(5)
    T = takeCommand()
    if T == "confirm":
        press("enter")
    else:
        quit()


def Whatsapp_VOICE_Call(name):
    speak("Opening What'sapp...")
    os.startfile(
        "C:\\Users\\Rudra\\OneDrive\\Desktop\\WhatsApp - Shortcut.lnk")
    sleep(5)
    pyautogui.click(x=195, y=115)
    sleep(1)
    speak("Making Search...")
    write(name)
    sleep(1)
    pyautogui.click(x=188, y=249)
    sleep(1)
    pyautogui.click(x=915, y=952)
    sleep(1)
    pyautogui.click(x=1198, y=63)
    sleep(1)
    speak("Making call...")
    press("enter")


def Whatsapp_VIDEO_Call(name):
    speak("Opening What'sapp...")
    os.startfile(
        "C:\\Users\\Rudra\\OneDrive\\Desktop\\WhatsApp - Shortcut.lnk")
    sleep(10)
    pyautogui.click(x=195, y=115)
    sleep(1)
    speak("Making search...")
    write(name)
    sleep(1)
    pyautogui.click(x=188, y=249)
    sleep(1)
    pyautogui.click(x=915, y=952)
    sleep(1)
    pyautogui.click(x=1658, y=105)
    sleep(1)
    speak("Do You Really Want Place The Video Call.....")
    press("enter")


def Location():
    speak("Opening Google Map...")
    os.startfile("https://www.google.com//maps")
    sleep(8)
    speak("Which Place Do You Want To Surf...")
    while True:
        q2=takeCommand().lower()
        if "current location" in q2:
            speak("Showing Your Current Location")
            pyautogui.click(x=1782, y=819)
            sleep(1)
            pyautogui.click(x=917, y=565)
            sleep(1)
            pyautogui.click(x=918, y=564)
            sleep(1)
            pyautogui.click(x=917, y=562)
            sleep(1)
            pyautogui.click(x=968, y=889)
            sleep(3)
            pyautogui.click(x=671, y=803)
            sleep(1)

        elif "location of" in q2:
            speak("Which Place Do You Want To Search")
            place=takeCommand().lower()
            pyautogui.click(x=181, y=153)
            sleep(1)
            write(place)
            sleep(1)
            press("enter")

        elif "exit" in q2:
            pyautogui.hotkey('ctrl','W')
            speak("Exiting From Site...")
            continue


def YTSearch(search):
    speak("Opening Youtube...")
    os.startfile("C:\\Users\\Rudra\\OneDrive\\Desktop\\YouTube.lnk")
    sleep(5)
    pyautogui.click(x=656, y=73)
    sleep(1)
    speak("Making Search...")
    write(search)
    sleep(1)
    press("enter")


def Songs(name):
    speak("Opening Spotify...")
    os.startfile("C:\\Users\\Rudra\\OneDrive\\Desktop\\\Spotify.lnk")
    sleep(5)
    pyautogui.click(x=41, y=154)
    sleep(1)
    pyautogui.click(x=589, y=48)
    sleep(1)
    write(name)
    sleep(1)
    pyautogui.click(x=1148, y=301)
    sleep(1)
    pyautogui.click(x=1148, y=301)
    sleep(1)
    quit()


async def getweather():
    speak("For Which City Do You Want To Know The WHEATHER..")
    w=takeCommand().lower()
    # declare the client. format defaults to the metric system (celcius, km/h, etc.)
    async with python_weather.Client(format=python_weather.IMPERIAL) as client:

        # fetch a weather forecast from a city
        weather = await client.get(w)

        # returns the current day's forecast temperature (int)
        print(weather.current.temperature)
        speak(weather.current.temperature)

        # get the weather forecast for a few days
        for forecast in weather.forecasts:
            print(forecast.date, forecast.astronomy)
            speak(forecast.date)
            speak( forecast.astronomy)

            # hourly forecasts
            for hourly in forecast.hourly:
                print(f' --> {hourly!r}')
                speak(f' --> {hourly!r}')


def res(query):
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif "open whatsapp" in query:
        speak("Opening What'sapp...")
        os.startfile(
            "C:\\Users\\Rudra\\OneDrive\\Desktop\\WhatsApp - Shortcut.lnk")
    elif "open google" in query:
        speak("Opening Google Chrome...")
        os.open("C:\\Users\\Public\\Desktop\\Google Chrome.lnk")
        while True:
            speak("What Do You Want To Search??")
            rep=takeCommand().lower()
            if "search" in rep:
                rep=rep.replace("search","")
                cq=takeCommand().lower()
                pyautogui.write(cq)
                press("enter")
            
            elif "exit" in rep:
                pyautogui.hotkey('ctrl','W')
                speak("Exiting From Site...")
                continue
    elif "open vs code" in query:
        speak("Opening Visual Studio Code...")
        os.startfile(
            "C:\\Users\\Rudra\\OneDrive\\Desktop\\Visual Studio Code.lnk")
    elif "show your code" in query:
        speak("Opening Code...")
        os.startfile(
            "C:\\Users\\Rudra\\OneDrive\\Desktop\\My Project\\Jarvis.py")
    elif "shutdown" in query:
        speak("Do You Really ,Want To ShutDown the system??")
        s = takeCommand()
        if s == "no":
            quit()
        else:
            os.system("shutdown /s /t 1")
    elif "restart" in query:
        speak("Do You Really ,Want To Restart the system??")
        R = takeCommand()
        if R == "no":
            quit()
        else:
            os.system("shutdown /r /t 1")
    elif "album" in query:
        speak("Opening Album...")
        os.startfile("C:\\Users\\Rudra\\OneDrive\\Pictures")
    elif "open ChatGPT" in query:
        speak("Opening Chat_Gpt..")
        os.startfile(
            "C:\\Users\\Rudra\\OneDrive\\Desktop\\My Project\\ai.py")
    elif "turn on camera" in query:
        speak("Opening Camera..")
        os.startfile("C:\\Users\\Rudra\\OneDrive\\Desktop\\Camera.lnk")
    elif "exit " in query:
        speak("I'M Leaving ,Sir!!")
        quit()
    elif "voice call" in query:
        query = query.replace("voice call", "")
        name = query
        Whatsapp_VOICE_Call(name)
    elif "video call" in query:
        query = query.replace("video call", "")
        name = query
        Whatsapp_VIDEO_Call(name)
            # elif "location of" in query:
    elif "location" in query:
        Location()
    elif "play song" in query:
        query = query.replace("play song", "")
        name = query
        Songs(name)
    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)    
        speak(f"Sir, the time is {strTime}")
    elif "date" in query:
        strdate=datetime.datetime.now().strftime("%d/%m/%Y")
        print(strdate)
        speak(f"Sir,Today Is {strdate}")
    elif "play" in query:
        query=query.replace("play","")
        speak("Playing"+query)
        pywhatkit.playonyt(query)
    elif "message" in query:
        speak("Tell Me The Name Of Person Whom You Want To Send Message..")
        name=takeCommand().lower()
        if "ansh" in name:
            n="+91-7777903176"
        elif "mom" in name:
            n="+91-7984947689"
        elif "dad" in name:
            n="+91-9601703173"
        elif "harsh" in name:
            n="+91-7984140706"
        elif "harshil" in name:
            n="+91-9313203015"
        elif "pruthak" in name:
            n="+91-9328520404"
        elif "om" in name:
            n="+91-9327910041"
        


        speak("What's Message..")
        msg=takeCommand().lower()
        pywhatkit.sendwhatmsg_instantly(phone_no=n,message=msg)
    elif "joke" in query:
        a=get_joke()
        print(a)
        speak(a)
    elif "weather" in query:
        if os.name == "nt":
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

            asyncio.run(getweather())


if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()
        res(query)

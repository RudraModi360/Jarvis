import python_weather
import asyncio
import os
import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

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

if __name__ == "__main__":
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(getweather())
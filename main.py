import pyttsx3 as p
import speech_recognition as sr
import WikiSearching as ws
import YtSearching as ys
import News as ns
import randfacts
import Joke as jk
import Weather as wt
import datetime


engine = p.init()
#voices = engine.getProperty("voices")
#engine.setProperty("voice",voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()
r = sr.Recognizer()


def TimeWiseWish():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning Engineer Rakib Hasan")
    elif hour>=12 and hour<16:
        speak("Good Afternoon Engineer Rakib Hasan")
    else:
        speak("Good Evenig Engineer Rakib Hasan")
today_date = datetime.datetime.now()
TimeWiseWish()


speak("I'm your voice assistant MOTU.")
speak("Today is "+today_date.strftime("%d")+ "of" +today_date.strftime("%B")+",and it's currently "+(today_date.strftime("%I"))+(today_date.strftime("%M"))+(today_date.strftime("%p")))
speak("Temparature in Dhaka is"+str(wt.temp())+"and with"+str(wt.des()))
speak("How are you sir?")


#for greetings
with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source,1.2)
    print("I'm Listening...")
    speak("I'm Listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
if "What" and "about" and "you" in text:
    speak("I'm also doing great sir.")
speak("How can I help you?")

#listening your words
while True:
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source,1.2)
        print("I'm Listening...")
        speak("I'm Listening...")
        audio = r.listen(source)
        text2 = r.recognize_google(audio)
        print(text2)


    #checking your word
    if "information" in text2:
        speak("Okay. Tell me what do you want know.")
        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print("I'm Listening...")
            speak("I'm Listening...")
            audio = r.listen(source)
            text3 = r.recognize_google(audio)
            print(text3)
        print("Searching {} in wikipedia".format(text3))
        speak("Searching {} in wikipedia".format(text3))
        a = ws.info()
        a.get_info(text3)


    #for youtube search
    elif "play" and "video" in text2:
        speak("Okay. Tell me the name of the song that you want to listen.")
        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print("I'm Listening...")
            speak("I'm Listening...")
            audio = r.listen(source)
            text3 = r.recognize_google(audio)
            print(text3)
        print("PLaying {} on youtube".format(text3))
        speak("PLaying {} on youtube".format(text3))
        b = ys.music()
        b.play(text3)


    elif "news" in text2:
        print("I,m searching top news of today in BBC...")
        speak("I,m searching top news of today in BBC...")
        print("Got the top news of today sir.")
        speak("Got the top news of today sir.")
        arr = ns.news()
        for i in range(len(arr)):
            print(arr[i])
            speak(arr[i])


    elif "fact" in text2:
        print("I'm searching a fact for you...")
        speak("I'm searching a fact for you...")
        print("Got a fact for you sir.")
        speak("Got a fact for you sir.")
        x = randfacts.get_fact()
        print(x)
        speak("Did you know that, "+x)


    elif "joke" in text2:
        print("I'm searching a joke for you...")
        speak("I'm searching a joke for you...")
        print("Got a joke for you sir.")
        speak("Got a joke for you sir.")
        arr = jk.joke()
        print(arr[0])
        speak(arr[0])
        print(arr[1])
        speak(arr[1])


    elif "stop" in text2:
        print("Okay sir, I'm gonna OFF within few seconds. Have a good day!")
        speak("Okay sir, I'm gonna OFF within few seconds. Have a good day!")
        exit()
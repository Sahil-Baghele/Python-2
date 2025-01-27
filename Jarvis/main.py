import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "9873c6c8f42a466ca2b97c74db65fa70"


def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    import openai
    client = openai.OpenAI(api_key="")

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:

            data = r.json()
            
            articles = data.get('articles', [])
            
            for article in articles:
                speak(article['title'])

            else:
                output = aiProcess(c)
                speak(output) 

if __name__ == "__main__":
    speak("Initializing Jarvis....")

    while True:
    
        r = sr.Recognizer()
            
        
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)     
            if(word.lower() == "jarvis"):
                speak("Yeah")

                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)  
                    command = r.recognize_google(audio)  

                    processCommand(command)   
    
        except Exception  as e:
            print("error; (0)".format(e))
            
                
                
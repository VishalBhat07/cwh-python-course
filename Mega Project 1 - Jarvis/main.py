import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
from client import AIprocess
from news import getTopHeadlines
from clean import clean_text

recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)


def speak(text):

    engine.say(text)
    engine.runAndWait()


def processCommand(c):

    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open gpt" in c.lower():
        webbrowser.open("https://chatgpt.com/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        webbrowser.open(musicLibrary.music[song])
    elif "news" in c:
        speak("Fetching news might take a moment")
        articles = getTopHeadlines()

        for article in articles:
            speak(article['title'])

    else:
        output = AIprocess(c)
        if "write" in c.lower():
            speak("Please see the terminal and tell me if you require any explanation")
            print(output)
        else:
            output = clean_text(output)
            speak(output)


if __name__ == "__main__":
    speak("Initializing apollo for your system...")

    while True:

        try:
            with sr.Microphone() as source:
                print("Listening...")
                # Adjusted settings for better recognition
                audio = recognizer.listen(
                    source, timeout=5, phrase_time_limit=3)
                word = recognizer.recognize_google(audio)

                if word.lower() == "apollo":
                    speak("Hi I am apollo, how may I help you")
                    print("Apollo Active...")
                    audio = recognizer.listen(
                        source, timeout=5, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio)
                    speak("Processing your request. Please wait...")
                    processCommand(command)

        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")

        except sr.RequestError as e:
            print(
                f"Could not request results from Google Speech Recognition service; {e}")

        except Exception as e:
            print(f"Error: {e}")

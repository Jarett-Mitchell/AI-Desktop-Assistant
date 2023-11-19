import speech_recognition as sr
from googlesearch import search


def googleSearch(Query):  # search using google lib
    for result in search(Query, num_results=5, stop=5, pause=2):
        print(result)


# initialize recognition
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak")
    audio = recognizer.listen(source)

try:  # test if speech was recognized
    print("You said: " + recognizer.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio")
except sr.RequestError as e:
    print(
        "Could not request results from Google Speech Recognition service; {0}".format(e))

try:  # search google if commanded FIXME
    recognized_text = recognizer.recognize_google(audio).lower()
    if "search google" or "Google search" in recognized_text:
        with sr.Microphone() as source:
            print("what for?")
            searchRecognizer = recognizer.listen(source)
            googleSearch(recognizer.recognize_google(searchRecognizer))
except:
    print("search failed...")

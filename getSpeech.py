import speech_recognition as sr
from googlesearch import search


def googleSearch(Query, numberOfResults):
    pass


recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak")
    audio = recognizer.listen(source)

# if "search google" in audio:
#     print('What would you like to search for?')
#     query = recognizer.listen(source)
#     print('How many results would you like?')
#     resultNumbers = recognizer.listen(source)
#     googleSearch()

try:
    print("You said: " + recognizer.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio")
except sr.RequestError as e:
    print(
        "Could not request results from Google Speech Recognition service; {0}".format(e))

try:
    recognized_text = recognizer.recognize_google(audio).lower()
    if "search google" in recognized_text:
        print("what for?")
        searchRecognizer = recognizer.listen(source)
        print(recognizer.recognize_google(searchRecognizer))
except:
    print("search failed...")

import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak")
    audio = recognizer.listen(source)

print(audio)

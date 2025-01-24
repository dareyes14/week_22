import pyttsx3 #pip install pyttsx3 == it is used to convert text to speech

engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

while True:
    text=input("Enter some text to convert text to speech: ")
    speak(text)
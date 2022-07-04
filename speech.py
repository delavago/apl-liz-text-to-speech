import pyttsx3
from tika import parser

# Text to speech function
def text_to_speech(txt):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.say(txt)
    engine.runAndWait()
    engine.stop()

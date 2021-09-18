import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
voices = engine.getProperty('voices')

engine.setProperty('rate', 160)
engine.setProperty('volume', 2)
engine.setProperty('voice', voices[1].id)

engine.say("""
Tests
""")
engine.runAndWait()
#pip install pyttsx3 en terminal
#pip install pyaudio
#pip install SpeechRecognition
#pip install soundfile
import pyttsx3
engine = pyttsx3.init()
engine.say("Hola Mundo")
engine.runAndWait()

""" import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(f"Voice: {voice.name}")
    engine.setProperty('voice', voice.id)
    engine.say("Hola mundo")
engine.runAndWait() """
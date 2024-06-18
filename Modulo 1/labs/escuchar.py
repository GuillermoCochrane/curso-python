import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Hable!")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="es-ES")
        print("dijiste: " + text)
    except sr.UnknownValueError:
        print("Perdon, no entiendo lo que estás diciendo")
    except sr.RequestError as e:
        print("Lo siento, hubo un error al comunicarse con el servicio de Google: " + e.message)
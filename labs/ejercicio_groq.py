from groq import Groq
#import pyttsx3


API_KEY = "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"

while True:
    pregunta = input("¿Qué pregunta quieres hacer? (escriba 'Salir' o 'Q' para salir): ").capitalize()
    if pregunta == "Salir" or pregunta == "Q":
        exit("Gracias por usar nuestro servicio!!")

    cliente = Groq(
        api_key = API_KEY,
    )

    chat_interaccion = cliente.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": pregunta,
            }
        ],
        model="llama3-8b-8192",
    )

    salida = chat_interaccion.choices[0].message.content
#    engine = pyttsx3.init()
#    engine.say(salida)
#    engine.runAndWait()
    print(salida)
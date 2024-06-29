# 🔮Adivina el numero🔮 Realizar un programa que adivine un numero con 3 intentos para adivinar el numero secreto entre 1 y 10
import random
numero_secreto =  random.randint(1,10)

print ("Bienvenido al juego de las adivinzas, tiene 3 intentos para adivinar el numero secreto que va a del 1 al 10")
nombre_usuario = input("¿Como te llamas?: ")
mensaje_error =f" {nombre_usuario}!!! Debes ingresar un numero del 1 al 10"
contador = 3

while contador != 0:

    while True:
        numero_usuario = input("Ingrese el numero a adivinar del 1 al 10: ")    
        #Validación de que el dato ingresado es un numero y no letras
        if numero_usuario.isdigit():
            numero_usuario = int(numero_usuario)
            #Validación de que el numero ingresado sea entre el rango permitido
            if numero_usuario <1 or  numero_usuario >10:
                print(mensaje_error)
            else:
                break
        else:
            print(mensaje_error)

    if numero_secreto == numero_usuario:
        print(f"¡¡Felicidades {nombre_usuario}, adivinaste el número!!")
        break
    else:
        print(f"Lo siento {nombre_usuario} , no adivinaste el número secreto, volve a intentarlo 🚀")
        contador -= 1
        print(f"Te queda {contador} oportunidades")
    
if contador == 0:
    print(f"Lo siento {nombre_usuario} , no adivinaste el número secreto")
    print(f"El número secreto era {numero_secreto}")
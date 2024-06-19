import random

print("")
print("#"*80)

print("######                                                                    ######")
print("######                 Bienvenido a ADIVINE UN NÚMERO                     ###### ")
print("######                                                                    ######")
print("###### Tendrá 3 oportuniades para adivinar el numero que pense 🧐🚀       ######")
print("######                                                                    ######")
print("######                                                                    ######")
print("#"*80)
print("")
print("Presione una tecla para continuar...")
input() # Esperar a que el usuario presione una tecla
# Limpiar la pantalla
print("\n"*50)

numero_aleatorio = random.randint(1, 10)
contador = 0

# 1° intento
entrada = input("Ingrese el número que UD. cree que yo pensé, del 1 al 10: ")
if not entrada.isdigit():
    print(f"Error: Debe ingresar un número válido. Fíjate lo que pusiste: {entrada}")
    exit()
entrada = int(entrada)
if entrada < 1 or entrada > 10:
    print(f"Error: Debe ingresar un número entre 0 y 10. Fíjate lo que pusiste: {entrada}")
    exit()
#transpolarlo a todos los intentos
#guardar mensajes en variables y luego imprimirlos (print(var))

if entrada == numero_aleatorio:
    print("¡Felicitaciones! ¡Lo has adivinado! 🌟")
    print(f"El número que pensaste era {numero_aleatorio}!")
    print(f"Y cometiste {contador} errores!")
    exit()
elif entrada > (numero_aleatorio + 3) or entrada < (numero_aleatorio - 3):
    print("Frío ❄, estás lejos del número.")
    contador += 1
    print(f"Y te quedan {3-contador} intentos más.")
else:
    print("Caliente 🔥, estás muy cerca del número.")
    contador += 1
    print(f"Y te quedan {3-contador} intentos más.")

# 2° intento:
if contador == 1:
    entrada = input("Ingrese el número que UD. cree que yo pensé: ")
    if not entrada.isdigit():
        print(f"Error: Debe ingresar un número válido. Fíjate lo que pusiste: {entrada}")
        exit()

    entrada = int(entrada)

    if entrada == numero_aleatorio:
        print("¡Felicitaciones! ¡Lo has adivinado!")
        print(f"El número que pensaste era {numero_aleatorio}!")
        print(f"Y cometiste {contador} errores!")
        exit()
    elif entrada > (numero_aleatorio + 3) or entrada < (numero_aleatorio - 3):
        print("Frío, estás lejos del número.")
        contador += 1
        print(f"Y te quedan {3-contador} intentos más.")
    else:
        print("Caliente, estás muy cerca del número.")
        contador += 1
        print(f"Y te quedan {3-contador} intentos más.")

# 3° intento:
if contador == 2:
    entrada = input("Ingrese el número que UD. cree que yo pensé: ")
    if not entrada.isdigit():
        print(f"Error: Debe ingresar un número válido. Fíjate lo que pusiste: {entrada}")
        exit()

    entrada = int(entrada)

    if entrada == numero_aleatorio:
        print("¡Felicitaciones! ¡Lo has adivinado!")
        print(f"El número que pensaste era {numero_aleatorio}!")
        print(f"Y cometiste {contador} errores!")
        exit()
    elif entrada > (numero_aleatorio + 3) or entrada < (numero_aleatorio - 3):
        print("Frío, estás lejos del número.")
        contador += 1
        print(f"Y te quedan {3-contador} intentos más.")
    else:
        print("Caliente, estás muy cerca del número.")
        contador += 1
        print(f"Y te quedan {3-contador} intentos más.")

# Si no se acertó el número:
if contador == 3:
    print("No has adivinado el número.")
    print(f"El número era {numero_aleatorio}!")
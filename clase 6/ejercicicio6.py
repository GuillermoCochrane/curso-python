# Realizar un juego de Cara o Cruz donde el usuario tenga 2 opciones para elegir, si jugar contra la computadora o un amigo. Si elige la segunda deberíamos preguntarle el nombre a ambos
import random
print("Bienvenido al juego de Cara o Cruz")
versus = input("¿Quieres jugar contra la computadora o un amigo? ").capitalize()
computadora = random.randint(1,2)
usuario = 0
seleccion_computadora = ""
if computadora == 1:
    seleccion_computadora = "Cara"
elif computadora == 2:
    seleccion_computadora = "Cruz"
    
if versus == "Computadora":
    seleccion_usuario = input("Escribe el que quieras seleccionar: Cara, o Cruz: ").capitalize()
    if seleccion_usuario == "Cara":
        usuario = 1
    elif seleccion_usuario == "Cruz":
        usuario = 2
    else:
        print("Lo siento, no seleccionaste un valor correcto")
        exit()
        
    if usuario == computadora:
        print(F"Salió {seleccion_computadora} y ganaste!!")
    else:
        print(F"Perdiste, porque salió {seleccion_computadora}")

elif versus == "Amigo":
    jugador1 = input("Que el jugador 1 ingrese su nombre: ").capitalize()
    jugador2 = input("Que el jugador 2 ingrese su nombre: ").capitalize()
    eleccion_usuario = input(f"{jugador1}, escribe lo que quieras seleccionar, Cara, o Cruz: ").capitalize()

    if eleccion_usuario == "Cara":
        print(f"{jugador1} eligio Cara, por lo tanto {jugador2} le queda Cruz")
        usuario = 1
    elif eleccion_usuario == "Cruz":
        print(f"{jugador1} eligio Cruz, por lo tanto {jugador2} le queda Cara")
        usuario = 2
    else:
        print("Lo siento, no seleccionaste un valor correcto")
        exit()

    if usuario == computadora:
        print(f"Salió {seleccion_computadora}")
        print(f"El ganador es {jugador1}")
    else:
        print(f"Salió {seleccion_computadora}")
        print(f"El ganador es {jugador2}")

else:
    print("Lo siento, no seleccionaste un valor correcto")
    exit()
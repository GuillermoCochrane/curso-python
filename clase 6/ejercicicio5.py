# Realizar un juego de piedra, papel y tijera.
import random
print("Bienvenido al juego de piedra, papel y tijera")
seleccion_usuario = input("Escribe el que quieras seleccionar: Piedra, Papel o Tijera: ").capitalize()

computadora = random.randint(1,3)
usuario = 0
seleccion_computadora = ""

if computadora == 1:
    seleccion_computadora = "Piedra"
elif computadora == 2:
    seleccion_computadora = "Papel"
elif computadora == 3:
    seleccion_computadora = "Tijera"


if seleccion_usuario == "Piedra" or seleccion_usuario == "Papel" or seleccion_usuario == "Tijera":
    if seleccion_usuario == "Piedra":
        usuario = 1
    elif seleccion_usuario == "Papel":
        usuario = 2
    elif seleccion_usuario == "Tijera":
        usuario = 3
    else:
        print("Lo siento, no seleccionaste un valor correcto")
        exit()

if computadora < usuario or (computadora == 3 and usuario == 1):
    print(f"¡¡Ganaste!! Elegiste: {seleccion_usuario} y yo elegí: {seleccion_computadora}")
elif computadora == usuario:
    print(f"Empate, elegimos lo mismo: {seleccion_usuario}")
else:
    print(f"Perdiste, elegiste {seleccion_usuario} y yo elegí {seleccion_computadora}")
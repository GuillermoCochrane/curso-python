import random

lista_alumnos = ["Monica", "maricel", "carlos", "guillermo" ]
#resto_alumnos = ["paula", "fermin", "gonzalo", "javier", "Jonathan", "florencia", "leticia", "shirley", "patricia", "marcelo"]
alumnos_pasados = lista_alumnos.copy()
continuar_seleccion = True

while True:
    largo_lista = len(alumnos_pasados) - 1
    rand = random.randint(0, largo_lista)
    alumno_seleccionado = alumnos_pasados[rand]
    print(f"\nEl alumno seleccionado es: {alumno_seleccionado}")
    alumnos_pasados.remove(alumno_seleccionado)
    
    if len(alumnos_pasados) == 0:
        exit("Ya no quedan alumnos para elegir")

    continuar = input("¿Desea seleccionar otro alumno?(s/n): ").lower()
    if continuar == "s":
        continuar_seleccion = True
    elif continuar == "n":
        continuar_seleccion = False
        break
    else:
        print("Opción no válida, por favor ingrese 's' o 'n'")
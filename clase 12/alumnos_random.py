import random

lista_alumnos = ["Monica", "Maricel", "Carlos", "Guillermo"]
#resto_alumnos = ["paula", "fermin", "gonzalo", "javier", "Jonathan", "florencia", "leticia", "shirley", "patricia", "marcelo"]
alumnos_pasados = []
largo_lista = len(lista_alumnos) - 1
continuar_seleccion = True

while True:
    while continuar_seleccion:
        rand = random.randint(0, largo_lista)
        alumno_seleccionado = lista_alumnos[rand]

        if alumno_seleccionado not in alumnos_pasados:
            print(f"El alumno seleccionado es: {alumno_seleccionado}")
            alumnos_pasados.append(alumno_seleccionado)
            continuar_seleccion = False

            if len(alumnos_pasados) == len(lista_alumnos):
                exit("Ya no quedan alumnos para elegir")
        else:
            print(f"El alumno {alumno_seleccionado} ya fue seleccionado, seleccionaremos otro alumno")
            continue

    continuar = input("¿Desea seleccionar otro alumno? (s/n): ")
    print("\n")
    if continuar.lower() == "s":
        continuar_seleccion = True
    elif continuar.lower() == "n":
        continuar_seleccion = False
        break
    else:
        print("Opción no válida, por favor ingrese 's' o 'n'")
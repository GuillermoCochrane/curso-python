# Escribe un programa que cuente una historia interactiva (del estilo de los libros "Elije tu propia aventura"), en el que el lector vaya leyendo la historia y llegado a cierto punto, tenga que elegir como sigue la historia. Dependiendo de las elecciones tomadas,  tendra diferentes finales. 

opcion = 0
titulo2 = "\nCapítulo 2: La Aventura Continúa\n"
capitulo2 = "Decides continuar con el curso y te sumerges más profundamente en el mundo de Python. Aprendes sobre estructuras de datos, funciones y bucles mientras resuelves problemas cada vez más complejos. Tu entusiasmo por la programación crece a medida que adquieres nuevas habilidades.\n"
selecion2 = "¿Quieres seguir adelante con el curso y enfrentar el desafío final del proyecto final? (Aprieta la tecla 4 Enter )\n ¿O te sientes frustrado y decides renunciar? (Aprieta la tecla 3 y Enter)\n"
titulo3 = "\nÚlitmo Capítulo 3: El Desafío Final\n"
capitulo3 = "Llega el momento de enfrentar el proyecto final del curso. Te enfrentas a un problema complicado que requiere todas las habilidades que has aprendido hasta ahora. Trabajas duro y, con determinación, logras completar el proyecto con éxito. Tu confianza en tus habilidades de programación está en su punto más alto y estás listo para enfrentar nuevos desafíos en el futuro. ¡Felicidades, has alcanzado el Final Feliz!\n"
titulo4 = "\nÚltimo Capítulo: El triste Final\n"
capitulo4 = "Decides abandonar el curso de programación y te sientes desanimado por no haber alcanzado tus metas. Sin embargo, con el tiempo, te das cuenta de que todavía hay oportunidades para aprender y crecer en el mundo de la informática.\n"
error = "\nOpción no válida\n"
fin = "\nFin\n"

print("\nEl viaje de programación en Python\n")
print("Eres un estudiante de la UP en General Levalle y te has inscrito en el curso de programación I en Python. Estás emocionado por aprender un nuevo lenguaje de programación y explorar el mundo de la informática.\n")
print("Capítulo 1: El Comienzo\n")
print("Comienzas el curso de programación y te encuentras con dos profesores ntusiastas que te introduce a los conceptos básicos de Python. Te enfrentas a desafíos emocionantes y aprendes a escribir tus primeros programas.\n")

while True:
    opcion1 = input("¿Quieres seguir adelante con el curso? (Ve al Capítulo 2 apretando la tecla 2 y Enter )\n ¿O te sientes abrumado y decides abandonar? (Aprieta la tecla 3 y Enter)\n")
    if opcion1.isdigit():
        if int(opcion1) == 2:
            print(titulo2)
            print(capitulo2)
            while True:
                opcion2 = input(selecion2)
                if opcion2.isdigit():
                    if int(opcion2) == 4:
                        print(titulo3)
                        print(capitulo3)
                        exit(fin)
                    elif int(opcion2) == 3:
                        print(titulo4)
                        print(capitulo4)
                        exit(fin)
                    else:
                        print(error)
                else:
                    print(error)
        elif int(opcion1) == 3:
            print(titulo4)
            print(capitulo4)
            exit(fin)
        else:
            print(error)
    else:
        print(error)


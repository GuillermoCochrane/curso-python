#Ejemplo NOT (mismo ejercicio pero invierta el resultado)
dia = input("Ingrese el dia de de la semana: ").capitalize()
if not (dia == "Sabado") and not(dia == "Domingo"):
    vacaciones = input("¿Se encuentra de vacaciones? ").capitalize()
    if not (vacaciones == "Si"):
        print(f"No puede ir porque es {dia} y {vacaciones} se encuentra de vacaciones")
    else:
        print(f"Puede ir porque a pesar de que es {dia}, {vacaciones} se encuentra de vacaciones")
else:
    print(f"Puede ir porque es {dia}")
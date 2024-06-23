#Ejemplo NOT (mismo ejercicio pero invierta el resultado)
dia = input("Ingrese el dia de de la semana: ")
if not (dia == "Sabado") or not(dia == "Domingo"):
    print("No puede ir")
else:
    vacaciones = input("¿Se encuentra de vacaciones? ")
    if not (vacaciones == "Si"):
        print("No puede ir")
    else:
        print("Puede ir")
# revisar el ejercicio 5_9
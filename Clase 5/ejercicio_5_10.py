#Crear un programa que permita al usuario ingresar su edad y determine si esta entre los 20 (de 20 a 30 años) y los 40 años(de 40 a 50 años).

edad = int(input("Ingrese su edad: "))
if edad >= 20 and edad <= 30:
    print("Esta entre los 20 a 30 años")
elif edad >= 40 and edad <= 50:
    print("Esta entre los 40 a 50 años")
else:
    print("No esta ni entre los 20 a 30 años ni entre los 40 a 50 años")
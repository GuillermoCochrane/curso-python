#ordenar
contador = 0

edad_1 = input("Ingrese la edad del primer usuario: ")
if edad_1.isdigit():
    edad_1 = int(edad_1)
else:
    print("El usuario no ingresó un número")
    exit()

edad_2 = input("Ingrese la edad del segundo usuario: ")
if edad_2.isdigit():
    edad_2 = int(edad_2)
else:
    print("El usuario no ingresó un número")
    exit()    

edad_3 = input("Ingrese la edad del tercer usuario: ")
if edad_3.isdigit():
    edad_3 = int(edad_3)
else:
    print("El usuario no ingresó un número")
    exit()    

edad_4 = input("Ingrese la edad del cuarto usuario: ")
if edad_4.isdigit():
    edad_4 = int(edad_4)
else:
    print("El usuario no ingresó un número")
    exit()      





promedio = (edad_1 + edad_2 + edad_3 + edad_4) / 4

print("El promedio de edad es", promedio)

if edad_1 >= edad_2 and edad_1 >= edad_3 and edad_1 >= edad_4:
    print("Edad 1 es el mayor")
if edad_2 >= edad_1 and edad_2 >= edad_3 and edad_2 >= edad_4:
    print("Edad 2 es el mayor")     
if edad_3 >= edad_1 and edad_3 >= edad_2 and edad_3 >= edad_4:
    print("Edad 3 es el mayor")
if edad_4 >= edad_1 and edad_4 >= edad_2 and edad_4 >= edad_3:
    print("Edad 4 es el mayor")
    
if edad_1 <= edad_2 and edad_1 <= edad_3 and edad_1 <= edad_4:
    print("Edad 1 es el menor")
if edad_2 <= edad_1 and edad_2 <= edad_3 and edad_2 <= edad_4:
    print("Edad 2 es el menor")     
if edad_3 <= edad_1 and edad_3 <= edad_2 and edad_3 <= edad_4:
    print("Edad 3 es el menor")
if edad_4 <= edad_1 and edad_4 <= edad_2 and edad_4 <= edad_3:
    print("Edad 4 es el menor")

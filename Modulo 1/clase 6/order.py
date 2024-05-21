#Realizar un programa que permita el ingreso de 4 personas con su nombre y apellido, su dirección y la edad y muestre en pantalla cual es la persona(con todos los datos ingresados) ,  con mayor edad (y en que posición se cargo) y la de menor edad y en que posición se cargo (Por ejemplo Diego Markiewicz de 44 años, vive en General Levalle y  fue cargado en el registro número  3  y Xxxxxxxx de 15 años, vive en hdhdushshsge y fue cargado en el registro número 1)
contador = 0
nombre1 = input("Ingrese su nombre: ")
if not nombre1.isalpha():
    print("El dato ingresado deben ser letras")
apellido1 = input("Ingrese su apellido: ")
if not apellido1.isalpha():
    print("El dato ingresado deben ser letras")
edad1 = (input("Ingrese su edad: "))
if not edad1.isdigit():
    print("El dato ingresado debe ser un número")
else:
    edad1 = int(edad1)
direccion1 = input("Ingrese su direccion: ")
contador += 1
posicion1 = contador

# datos de la segunda persona
nombre2 = input("Ingrese su nombre: ")
if not nombre2.isalpha():
    print("El dato ingresado deben ser letras") 
apellido2 = input("Ingrese su apellido: ")
if not apellido2.isalpha():
    print("El dato ingresado deben ser letras")
else:
    edad2 = (input("Ingrese su edad: "))
if not edad2.isdigit():
    print("El dato ingresado debe ser un número")
edad2 = int(edad2)
direccion2 = input("Ingrese su direccion: ")
contador += 1
posicion2 = contador

# datos de la tercera persona
nombre3 = input("Ingrese su nombre: ")
if not nombre3.isalpha():
    print("El dato ingresado deben ser letras")
apellido3 = input("Ingrese su apellido: ")
if not apellido3.isalpha():
    print("El dato ingresado deben ser letras")
edad3 = (input("Ingrese su edad: "))
if not edad3.isdigit():
    print("El dato ingresado debe ser un número")
else:
    edad3 = int(edad3)
direccion3 = input("Ingrese su direccion: ")
contador += 1
posicion3 = contador

# datos de la cuarta persona
nombre4 = input("Ingrese su nombre: ")
if not nombre4.isalpha():
    print("El dato ingresado deben ser letras")
apellido4 = input("Ingrese su apellido: ")
if not apellido4.isalpha():
    print("El dato ingresado deben ser letras")
edad4 = (input("Ingrese su edad: "))
if not edad4.isdigit():
    print("El dato ingresado debe ser un número")
else:
    edad4 = int(edad4)
direccion4 = input("Ingrese su direccion: ")
contador += 1
posicion4 = contador

if edad1 > edad2 and edad1 > edad3 and edad1 > edad4:
    print(f"{nombre1} {apellido1} de {edad1} años, vive en {direccion1} y fue cargado en el registro numero {posicion1} es la persona con mayor edad")
elif edad2 > edad1 and edad2 > edad3 and edad2 > edad4:
    print(f"{nombre2} {apellido2} de {edad2} años, vive en {direccion2} y fue cargado en el registro numero {posicion2} es la persona con mayor edad")
elif edad3 > edad1 and edad3 > edad2 and edad3 > edad4:
    print(f"{nombre3} {apellido3} de {edad3} años, vive en {direccion3} y fue cargado en el registro numero {posicion3} es la persona con mayor edad")
elif edad4 > edad1 and edad4 > edad2 and edad4 > edad3:
    print(f"{nombre4} {apellido4} de {edad4} años, vive en {direccion4} y fue cargado en el registro numero {posicion4} es la persona con mayor edad")

edad_promedio = (edad1 + edad2 + edad3 + edad4) / contador

print(f"El promedio de edad es {edad_promedio}")

if edad1 < edad2 and edad1 < edad3 and edad1 < edad4:
    print(f"{nombre1} {apellido1} de {edad1} años, vive en {direccion1} y fue cargado en el registro numero {posicion1} es la persona con menor edad")
elif edad2 < edad1 and edad2 < edad3 and edad2 < edad4:
    print(f"{nombre2} {apellido2} de {edad2} años, vive en {direccion2} y fue cargado en el registro numero {posicion2} es la persona con menor edad")
elif edad3 < edad1 and edad3 < edad2 and edad3 < edad4:
    print(f"{nombre3} {apellido3} de {edad3} años, vive en {direccion3} y fue cargado en el registro numero {posicion3} es la persona con menor edad")
elif edad4 < edad1 and edad4 < edad2 and edad4 < edad3:
    print(f"{nombre4} {apellido4} de {edad4} años, vive en {direccion4} y fue cargado en el registro numero {posicion4} es la persona con menor edad")

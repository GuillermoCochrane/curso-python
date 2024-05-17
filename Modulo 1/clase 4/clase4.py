saludo = "hola"
print("saludo es", saludo)
otro_saludo = saludo
print("otro saludo es", otro_saludo)
cifra1 = 1
cifra2 = 2
resultado = cifra1 + cifra2
print("el resultado es", resultado)
print("cifra1 mas cifra2 es", cifra1 + cifra2)
numero = 15
print("el numero es", numero)
numero = 15 + 20
print("el nuevo valor numero es", numero)
print("la multiplicacion es: ", cifra1 * cifra2)
print("la division es: ", cifra1 / cifra2)
suma = cifra1 + 10
print("la suma es: ", suma)
modulo = cifra1 % cifra2
print("el modulo es: ", modulo)

bienvenida = "hola, "
despedida = "adios"
print("concatenamos",bienvenida+despedida);
print("si multiplicamos un string, lo repetimos: ", bienvenida*4)
print("el valor de cifra1 es: ", cifra1)
print(f"el valor de cifra2 es:  {cifra2}")#otra forma de concatenar variables con strings
'''cometamos multiples 
lineas'''

ingreso_teclado = input("ingrese su nombre: ")
print(f"Bienvenido, {ingreso_teclado}, a la clase 4")

numero1 = int(input("ingrese un numero: "))
numero2 = int(input("ingrese otro numero: "))


print("El resultado es de la suma es: ", numero1 + numero2)

nombre = input("ingrese su nombre: ")
otro_nombre = input("ingrese otro nombre: ");
frase = print(f"{nombre} y {otro_nombre} estudian programacion")
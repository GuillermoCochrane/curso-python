#❎ Tabla de Multiplicar: Realizar un programa que muestre la tabla de multiplicar de un número ingresado por el usuario.

numero = int(input("Ingrese un numero: "))
contador = 0
print(f"La tabla del {numero} es:")
while contador < 11:
    print(f"{numero} x {contador} = {numero * contador}")
    contador += 1
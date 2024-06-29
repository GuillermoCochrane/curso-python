#💻 SUMADORA: Realizar un programa que permita sumar numeros hasta que se ingrese un 0
suma = 0
while True:
    numero = input("Ingrese un numero: ")
    if numero == "0":
        print(f"La suma total es: {suma}")
        break
    else:
        suma += int(numero)
        print(f"La suma parcial es: {suma}")
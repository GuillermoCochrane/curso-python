""" #solo numeros 
entrada = input("Ingrese un numero: ")
print(entrada)
print(type(entrada))
#entrada = int(entrada)
#print(entrada)
#7
# print(type(entrada))

numero = input("Ingrese un numero: ")
print(numero)
print(type(numero))

suma = entrada + numero
print(suma)
print(type(suma))
entrada = int(entrada)
numero = int(numero)
suma = entrada + numero
print(f"La suma de {entrada} y {numero} es {suma}")
print(type(suma)) """   

contador = 0
variable1 = input("Ingrese un numero: ")
variable1 = int(variable1)
variable2 = input("Ingrese otro numero: ")
variable2 = int(variable2)
suma = variable1 + variable2
contador = contador + 1
print(f"La suma de {variable1} y {variable2} es: {suma}")
print(f"El contador es {contador}")
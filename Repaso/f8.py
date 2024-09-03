# Funcion de encontrar el maximo entre 3 numeros
# cree una funcion que permita ingresar 3 números y nos muestre cual es el mayor

def el_mayor(numero1: int, numero2: int, numero3: int) -> int:
  """
  Funcion que nos muestre cual es el mayor entre 3 numeros
  """
  numero_mayor = numero1
  if numero_mayor < numero2 :
    numero_mayor = numero2
  if numero_mayor < numero3:
    numero_mayor = numero3
  return numero_mayor

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))
print(f"El mayor entre {numero1}, {numero2} y {numero3} es: {el_mayor(numero1, numero2, numero3)}")
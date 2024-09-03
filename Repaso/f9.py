# Generar una lista de números aleatorios:
# Generar un programa que permita el ingreso de la cantidad de numeros aleatorios a generar y los muestre
import random

def lista_aleatoria(numero: int | None = 1, rango: int | None = 100) -> list:
  """
  Funcion que genera una lista de N números aleatorios positivos, donde N es el numero de numeros a generar, y el rango es el rango de los números aleatorios. Si no se ingresa el numero, se usará el valor por defecto de 1, y si no se ingresa el rango, se usará el valor por defecto de 100
  """
  lista_aleatoria = []
  for i in range(numero):
    lista_aleatoria.append(random.randint(1, rango))
  return lista_aleatoria

numero = int(input("Ingrese la cantidad de numeros aleatorios a generar: "))
rango = int(input("Ingrese el rango de los números aleatorios: "))
print(f"La lista de números aleatorios generados son: {lista_aleatoria(numero, rango)}")
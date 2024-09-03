# Funcion de Calculo Factorial. (Facil)
# Escribe una funcion que calcule el factorial de un numero dado.
# El factorial de un número entero positivo se define como el producto de todos los enteros positivos menores o iguales al número, Ejemplo: Factorial de 4 = 24(4
# x 3 x 2 x 1)

def factorial(numero: int) -> int:
  """
  Funcion que calcule el factorial de un numero dado
  """
  if numero < 0:
    return "El numero debe ser positivo"
  elif numero == 0:
    return 1
  else:
    factorial = 1
    lista_parcial = []
    for i in range(1, numero + 1):
      factorial *= i
      lista_parcial.append(factorial)
    return [lista_parcial, factorial]

numero = int(input("Ingrese un numero: "))
print(f"El factorial de {numero} es {factorial(numero)[1]} y todos los resultados son {factorial(numero)[0]}")
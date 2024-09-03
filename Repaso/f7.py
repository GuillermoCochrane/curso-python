# Funcion de Secuencia Fibonacci (Medio)
# Desarrolla una funcion que genere una lista con los primeros 'n' numeros de la secuencia de Fibonacci, donde cada numero es la suma de los dos anteriores comenzando con 0 y 1.
# Ejemplo el decimo número de la secuencia es: 34

def fibonacci(numero: int) -> list:
  """
  Funcion que genere una lista con los primeros 'n' numeros de la secuencia de Fibonacci, donde cada numero es la suma de los dos anteriores comenzando con 0 y 1
  """
  if numero < 0:
    numero = int(input("El numero debe ser positivo, ingrese un numero: "))
  elif numero == 0:
    return [0]
  elif numero == 1:
    return [0, 1]
  else:
    lista_fibonacci = [0, 1]
    aurea = []
    for i in range(2, numero):
      lista_fibonacci.append(lista_fibonacci[i-1] + lista_fibonacci[i-2])
      if lista_fibonacci[i-2] != 0:
        aurea.append(lista_fibonacci[i-1] / lista_fibonacci[i-2])
      # aureo = aurea.pop()
    return [lista_fibonacci, lista_fibonacci[numero-1], aurea[i-3]  ]

numero = int(input("Ingrese un numero: "))
print(f"Los primeros {numero} numeros de la secuencia de Fibonacci son: {fibonacci(numero)[0]} y el {numero}º número es: {fibonacci(numero)[1]} y el número aureo aproximado es: {fibonacci(numero)[2]}")
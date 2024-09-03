#Función Verificar si un número es par o impar.

def es_par_o_impar(numero: int | None = 0) -> bool:
  """
  Función que devuelve True si el número es par y False si es impar
  """
  if numero % 2 == 0:
    return True
  else:
    return False

numero = int(input("Ingrese un número: "))
print(f"El número {numero} es {'par' if es_par_o_impar(numero) else 'impar'}")
# Crea una funcion para calcular el área de un cuadrado

def area(lado: int | None = 0) -> int:
  """
  Función que devuelve el area de un cuadrado
  """
  return lado * lado

def perimetro(lado: int | None = 0) -> int:
  """
  Función que devuelve el perímetro de un cuadrado
  """
  return lado * 4

lado = 5
print(f"El area de un cuadrado es {area(lado)}")
print(f"El perímetro de un cuadrado es {perimetro(lado)}")
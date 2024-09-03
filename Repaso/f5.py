# Función de conversión de Temperatura. (Facil)
# Escribe una función que convierta la temperatura de Celsius a Fahrenheit y viceversa. La función debe aceptar dos argumentos: el valor de la temperatura y una cadena que indique si se está convirtiendo a Celsius('C') o a Fahrenheit('F').
#  Una ayuda practica ¡se necesita usar if, elif y else! formula celsius (temperatura - 32) * 5/9 formula Fahrenheit = temperatura * 9/

def temperatura(temperatura: float | None = 0, unidad: str | None = "C") -> float:
  """
  Función que convierte la temperatura de Celsius a Fahrenheit y viceversa
  """
  while True:
    if unidad.upper() == "F":
      return [(temperatura * 9/5) + 32, unidad]
    elif unidad.upper() == "C":
      return [(temperatura - 32) * 5/9 , unidad]
    else:
      unidad = input("Debe ingresar 'C' o 'F': ")  

temperatura_original = float(input("Ingrese la temperatura a convertir: "))
unidad = input("¿Desea convertir a Fahrenheit (F) o Celsius (C)?: ")
temperatura_convertida = temperatura(temperatura_original, unidad)
print(f"La temperatura convertida es {temperatura_convertida[0]}°{temperatura_convertida[1].upper()}")
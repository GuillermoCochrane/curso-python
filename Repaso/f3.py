# Crea una funcion para ordenar una lista de palabras

def ordenar(palabras: list[str] | None = []) -> list[str]:
  """
  Función que devuelve una lista ordenada de palabras
  """
  return sorted(palabras)

palabras = ["perro", "gato", "raton", "manzana", "pescado", "aguacate"]
print(f"La lista ordenada es: {ordenar(palabras)}")
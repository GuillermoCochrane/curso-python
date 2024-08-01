# Nuestras funciones

# saludar (procedimiento)
def saludar(nombre:str | None = ",te olvidaste el parámetro "):
    print("Hola " + nombre)

# calcular area rectangulo (función)
def area_rectangulo(largo:int | None = 0, alto: int | None = 0) -> int:
    return largo * alto

saludar()
print(area_rectangulo())
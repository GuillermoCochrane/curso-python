# Nuestras funciones

import mis_funciones as mf

# saludar (procedimiento)
def saludar(nombre:str | None = ",te olvidaste el parámetro "):
    """
    Imprime un saludo con el nombre que se le ingresa como parámetro.
    Si no se le ingresa el parámetro, se imprime "Hola, te olvidaste el parámetro"
    """
    print("Hola " + nombre)

# calcular area rectangulo (función)
def area_rectangulo(largo:int | None = 0, alto: int | None = 0) -> int:
    """
    Calcula la área de un rectangulo con los parámetros que se le ingresan.
    Si no se le ingresan los parámetros, devuelve 0 (0 x 0)
    """
    if largo == 0 or alto == 0:
        largo = 1
        alto = 1
    return largo * alto

numero1 = mf.validador_de_numero()
numero2 = mf.validador_de_numero()
print(mf.sumar(numero1, numero2))
# saludar()
# print(area_rectangulo())
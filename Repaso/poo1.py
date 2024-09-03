# Ejercicio 1: Crear una Clase de Rectángulo
# Objetivo: Crear una clase llamada Rectangulo que tenga dos atributos: ancho y alto.

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def mensaje(self):
        return f"El rectangulo tiene un ancho de {self.ancho} y un alto de {self.alto}"

rect = Rectangulo(10, 20)
print(rect.mensaje())
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)
    
    def caracteristicas(self):
        print(f"El rectangulo tiene un ancho de {self.ancho} y un alto de {self.alto}, con un area de {self.area()} y un perímetro de {self.perimetro()}")

rect1 = Rectangulo(10, 20)
rect1.caracteristicas()
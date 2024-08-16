#definiendo objetos

class Vehiculos: 
    def __init__(self, color, marca , modelo, puertas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.puertas = puertas
        
    def mostrar_caracteristicas(self):
        print(f"El color de este {self.marca} {self.modelo} es {self.color} y tiene {self.puertas} puertas")
        
    def datos_vehiculo(self):
        return

class autos: 
    def __init__(self):
        self.color = "azul"
        self.marca = "Ford"
        self.modelo = "Fiesta"
        self.puertas = 4
        
    def mostrar_caracteristicas(self):
        print(f"El color de este {self.marca} {self.modelo} es {self.color} y tiene {self.puertas} puertas")

auto_diego = Vehiculos("rojo", "Ford", "Fiesta", 4)
auto_diego.mostrar_caracteristicas()
print(f"el color del auto es {auto_diego.color}")
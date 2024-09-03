# Ejercicio 3: Crear una Clase de Producto
# Objetivo: Crear una clase llamada Producto que tenga tres atributos: nombre, precio y cantidad. Y tenga 3 metodos, Actualizar Precio, Actualizar Cantidad y Calcular valor total, el primero modificara el precio del producto, el segundo la cantidad y el ultimo debera multiplicar la cantidad por el precio del producto seleccionado para saber el valor total del inventario.

class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def actualizar_precio(self, precio: float):
        """
        Metodo que actualiza el precio del producto.
        """
        self.precio = precio

    def actualizar_cantidad(self, cantidad: int):
        """
        Metodo que actualiza la cantidad del producto.
        """
        self.cantidad = cantidad

    def calcular_valor_total(self):
        """
        Metodo que calcula el valor total del producto.
        """
        return self.cantidad * self.precio

producto = Producto("Juego de ajedrez", 12, 3)
print(f"Se agregó al carrito {producto.cantidad} {producto.nombre}, que tiene un precio de ${producto.precio} , el costo total es del pedido es de ${producto.calcular_valor_total()}")

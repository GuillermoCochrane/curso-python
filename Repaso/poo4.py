# Ejercicio 4: Crear una Clase de Contador
# Objetivo: Crear una clase llamada Contador que tenga un atributo cuenta que empieza en 0. Y que posea4 metodos, Incrementar(sumará 1), Decrementar(restará 1, no admite negativos osea hasta maximo 0), Mostrar Contador(deberá devolver el valor actual de contador) y Reiniciar(volverá a cero el contador)

class Contador:
    def __init__(self):
        self.cuenta = 0
        pass

    def incrementar(self, cantidad: int = 1):
        """
        Metodo que incrementa la cuenta del contador.
        Si no se ingresa cantidad, se usará el valor por defecto de 1.
        """
        self.cuenta += cantidad
        return 

    def decrementar(self, cantidad: int = 1):
        """
        Metodo que decrementa la cuenta del contador.
        Si no se ingresa cantidad, se usará el valor por defecto de 1.
        """
        self.cuenta -= cantidad
        return

    def reiniciar(self):
        """
        Metodo que reinicia el contador a cero.
        """
        self.cuenta = 0
        return 
    
    def mostrar(self):
        """
        Metodo que devuelve el valor actual de la cuenta del contador.
        """
        return self.cuenta
      
    def mensaje(self):
        """
        Metodo que devuelve un mensaje con información sobre el contador.
        """
        return f"El contador actual es {self.mostrar()}"
      
contador = Contador()
contador.incrementar()
contador.incrementar()
contador.incrementar(4)
print(contador.mensaje())
contador.decrementar(3)
print(contador.mensaje())
contador.reiniciar()
print(contador.mensaje())
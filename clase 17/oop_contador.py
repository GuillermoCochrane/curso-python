class Contador:
    def __init__(self):
        self.valor = 0
        pass

    def aumentar(self, sumar: int | None = 1):
        self.valor += sumar
        return

    def diminuir(self,restar: int | None = 1):
        if (self.valor > 0):
            self.valor -= restar
        return

    def incrementar_x(self,x):
        for i in range(x):
            self.aumentar()
        return
    
    def decrementar_x(self,x):
        for i in range(x):
            self.diminuir()
        return

    def reiniciar(self):
        self.valor = 0
        return

    def mostrar(self):
        print(f"El valor actual del contador es {self.valor}")
        return

    def devolver(self):
        return self.valor

c = Contador()
c.aumentar()
c.mostrar()
c.diminuir()
c.mostrar()
c.reiniciar()
c.mostrar()
print(c.devolver())
c.incrementar_x(8)
c.mostrar()
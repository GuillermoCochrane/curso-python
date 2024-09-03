# Ejercicio 2: Crear una clase de Cuenta Bancaria
# Objetivo: Implementar una clase CuentaBancaria que permita a los usuarios realizar operaciones bancarias básicas como depositar, retirar y consultar el saldo.

class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def depositar(self, cantidad:int | None = 0)->int:
      """
      Metodo que permite a los usuarios depositar dinero en la cuenta bancaria.
      Si no se ingresa cantidad, se usará el valor por defecto de 0.
      """
      self.saldo += cantidad
      return self.saldo

    def retirar(self, cantidad: int | None = 0) -> int:
        """
        Metodo que permite a los usuarios retirar dinero de la cuenta bancaria.
        Si no se ingresa cantidad, se usará el valor por defecto de 0.
        """
        self.saldo -= cantidad
        return self.saldo

    def saldo_actual(self)->int:
        """
        Metodo que devuelve el saldo actual de la cuenta bancaria.
        """
        return self.saldo

    def mensaje(self):
        """
        Metodo que devuelve un mensaje con información sobre la cuenta bancaria.
        """
        return f"El saldo actual de la cuenta es {self.saldo_actual()}"

cuenta = CuentaBancaria(1000)
print(cuenta.mensaje())
print(f"Se realizo un deposito a la cuenta de {cuenta.depositar(500)}")
print(cuenta.mensaje())
print(f"Se realizo un retiro a la cuenta de {cuenta.retirar(200)}")
print(cuenta.mensaje())

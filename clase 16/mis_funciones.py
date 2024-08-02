def sumar(numero_1: str | None = 0, numero_2: str | None = 0) -> int:
    """
    suma los números que recibe como parámetros, 
    si no se recibe ningún parámetro, por defecto son 0,
    por lo que la función devuelve 0
    """
    return numero_1 + numero_2

def restar(numero_1: str | None = 0, numero_2: str | None = 0) -> int:
    """
    restr los números que recibe como parámetros, 
    si no se recibe ningún parámetro, por defecto son 0,
    por lo que la función devuelve 0
    """
    return numero_1 - numero_2

def multiplicar(numero_1: str | None = 0, numero_2: str | None = 0) -> int:
    """
    multiplica los números que recibe como parámetros, 
    si no se recibe ningún parámetro, por defecto son 0,
    por lo que la función devuelve 0
    """
    return numero_1 * numero_2

def dividir(numero_1: str | None = 0, numero_2: str | None = 1) -> int:
    """
    divide los números que recibe como parámetros, 
    si no se recibe ningún parámetro, por defecto son 0,
    por lo que la función devuelve 0
    """
    return numero_1 / numero_2

def validador_de_numero():
    """
    Función pide un número y los valida. Si no es válido, se imprime un mensaje y se vuelve a pedirle un número válido
    """
    while True:
        numero = input("Ingresa un número: ")
        if numero.isdigit():
            numero = int(numero)
            # return numero  # el return puede cumplir la misma función del break
            break
        else:
            print("Ingresa un número válido")
    return numero #en caso del return de arriba, este return no iria
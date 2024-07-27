# de 3 numeros que ingresemos, hacer una funcion que devuelve el mayor
def mayor(numero1, numero2, numero3):
    if numero1 > numero2 and numero1 > numero3:
        return numero1
    elif numero2 > numero1 and numero2 > numero3:
        return numero2
    else:
        return numero3

def entrada():
    while True:
        texto = input("Ingrese un numero: ")
        if texto.isdigit():
            return int(texto)
        else:
            print("Debe ingresar un numero")

primer_numero = entrada()
segundo_numero = entrada()
tercer_numero = entrada()
mayor_numero = mayor(primer_numero, segundo_numero, tercer_numero)

print(f"El mayor numero es {mayor_numero}")
entrada = input("Ingrese un numero: ")
#print(type(entrada))
#print(entrada.isdigit())
if entrada.isdigit():
    print(f"El numero ingresado es: {entrada}")
else:
    print("Error: debe ingresar un numero")
    
otra_entrada = input("Ingrese un texto: ")
if otra_entrada.isalpha() or otra_entrada.isspace():
    print(f"El texto ingresado es: {otra_entrada}")
else:
    print("Error: debe ingresar un texto")
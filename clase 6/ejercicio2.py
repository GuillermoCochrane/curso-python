# - Realizar un programa que permita ingresar solo texto y los muestre todo en mayuscula
entrada = input("Ingrese un texto: ")
if entrada.isdigit():
    print("Error: Debe ingresar solo texto.")
else:
    entrada_mayuscula = entrada.upper()
    print(f"el text ingresado es {entrada_mayuscula}.")
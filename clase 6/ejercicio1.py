# realizar un programa que permita ingresar solo texto
entrada = input("Ingrese un texto: ")

if entrada.isdigit():
    print("Error: Debe ingresar solo texto (letras o espacios).")
else:
    print(f"el text ingresado es {entrada}.")
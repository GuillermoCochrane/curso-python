# Realizar un programa que permita ingresar solo numeros, si no se cumple este requisito, que me de la hasta 2 oportunidades mas y me muestre la cantidad de veces que lo hice mal.
entrada = input("Ingrese un número: ")

if entrada.isdigit():
    print(f"el numero ingresado es {entrada}.")
else:
    print(f"Error: Debe ingresar un número válido. fijate lo que pusiste!{entrada}")
    entrada = input("Ingrese otro numero: ")
    if entrada.isdigit():
        print(f"el numero ingresado es {entrada}.")
    else:
        print(f"Error: Debe ingresar un número válido. fijate lo que pusiste!{entrada}")
        entrada = input("Ingrese otro numero: ")
        if entrada.isdigit():
            print(f"el numero ingresado es {entrada}.")
        else:
            print("Error: Debe ingresar un número válido. Se quedo sin oportunidades.")
            exit()
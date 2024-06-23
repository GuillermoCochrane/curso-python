# Crear un programa que permita que el usuario ingrese dos numeros enteros y nos imprima cual es el mayor de los dos numeros ingresados

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1 > num2:
    print("El numero mayor es el primero:", num1)
elif num1 < num2:
    print("El numero mayor es el segundo:", num2)
else:
    print("Los numeros son iguales")
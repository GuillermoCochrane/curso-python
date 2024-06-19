#A mi se me rompió la calculadora 😂 así que necesito que me hagan un programa que me permita ingresar tres valores, siendo los primeros dos los números a utilizar y el tercero indicará la operación matemática a realizar(S, R, M, D) necesitaría que cuando me imprima el resultado tenga el siguiente formato de salida: Operación realizada con éxito, el resultado de (Aquí debe mostrar que operación se realizó) es (aquí debe mostrar el resultado) tengan en cuenta que no se puede dividir por CERO así que me debería advertir si lo coloco en el segundo número
numero1 = (input("Ingrese el primer número: "))
if not numero1.isnumeric():
    print("el dato debe ser un número")
else:
    numero1 = int(numero1)
if numero1 % 2 == 0:
    print("el primer número es par")
elif numero1 % 2 != 0:
    print("el primer número es inpar")
else:
    print("el primer número es cero")

numero2 = (input("Ingrese el segundo número: "))
if not numero2.isnumeric():
    print("el dato debe ser un número")
else:
    numero2 = int(numero2)
if numero2 % 2 == 0:
    print("el segundo número es par")
elif numero2 % 2 != 0:
    print("el segundo número es inpar")
else:
    print("el segundo número es cero")
    
operacion = (input("Ingrese la operación que desea realizar suma (S), resta (R), multiplicación (M) o división (D): "))
if not operacion.isalpha():
    print("el dato debe ser una letra")
if operacion == "S" or operacion == "s":
    resultado = numero1 + numero2
    print("la suma se realizó con éxito")
    print("el resultado es: " + str(resultado))
elif operacion == "R" or operacion == "r":
    resultado = numero1 - numero2
    print("la resta se realizó con éxito")
    print("el resultado es: " + str(resultado))
elif operacion == "M" or operacion == "m":
    resultado = numero1 * numero2
    print("la multiplicación se realizó con éxito")
    print("el resultado es: " + str(resultado))
elif operacion == "D" or operacion == "d":
    if numero2 == 0:
        print("no se puede dividir por cero")
    else:
        resultado = numero1 / numero2
        print("la división se realizó con éxito")
        print("el resultado es: " + str(resultado))
else:
    print("No ingreso el caracter para una operación válida")
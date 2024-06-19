variable = ""
variable = input("Ingrese una palabra: ")
if variable.isdigit():
    print("Es un numero, era una palabra")
    exit()
else:
    print(f"La palabra ingresada es {variable}")
if not variable.isdigit():
    print(f"Es una palabra, {variable}, seguimos")
else:
    print("Es un numero, era una palabra")
    exit()

a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))
print(f"Si a es: {a} y b es: {b}")
resultado = (a == b) # comparar dos variables (igualdad)
print(f"El resultado es de 'a == b': {resultado}")

resultado_2 = (a != b) # comparar dos variables (diferencia)
print(f"El resultado de 'a != b' es: {resultado_2}")    

resultado_3 = (a < b) # comparar dos variables (menor)
print(f"El resultado de 'a < b' es: {resultado_3}")

resultado_4 = (a > b) # comparar dos variables (mayor)
print(f"El resultado de 'a > b' es: {resultado_4}")

resultado_5 = (a <= b) # comparar dos variables (menor o igual)
print(f"El resultado de 'a <= b' es: {resultado_5}")    

resultado_6 = (a >= b) # comparar dos variables (mayor o igual)
print(f"El resultado de 'a >= b' es: {resultado_6}")

edad = int(input("Ingrese su edad: "))
if edad >= 18 and edad <= 35:
    print(f"Puedes entrar  porque tienes {edad} anios y  eres mayor de 18 años")
elif edad <= 50 and edad >= 35:
    print(f"Con {edad} anios estas en la edad de justa")
elif edad <= 17: 
    print(f"anda a dormir porque tienes {edad} anos")
elif edad > 51:
    print(f"anda a dormir porque tienes {edad} anios")
else:
    print(f"Con {edad} años no puedes entrar")
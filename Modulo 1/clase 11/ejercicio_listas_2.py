# Ejercicio 2. Crear una lista de números y luego:
# Calcular la suma de todos los números de la lista.
# Encontrar el número máximo y mínimo de la lista.
# Multiplicar cada número de la lista por 2.
# Imprimir los números pares de la lista.

lista_numeros = [1, 23, 63, 14, 95, 46, 77, 8, 39, 51]
print("lista de números")
print(lista_numeros)
print("\n")

# Calcular la suma de todos los números de la lista.
suma_numeros = sum(lista_numeros)
print(f"suma de todos los números: {suma_numeros}")
print("\n")

# Encontrar el número máximo y mínimo de la lista.
numero_max = max(lista_numeros)
numero_min = min(lista_numeros)
print(f"número máximo: {numero_max}")
print("\n")
print(f"número mínimo: {numero_min}")
print("\n")

# Multiplicar cada número de la lista por 2.
lista_numeros_x_2 = [x * 2 for x in lista_numeros]
print(f"lista de números multiplicados por 2: {lista_numeros_x_2}")
print("\n")

# Imprimir los números pares de la lista.
for numero in lista_numeros:
    if numero % 2 == 0:
        print(f"El número {numero} es par")
print("\n")
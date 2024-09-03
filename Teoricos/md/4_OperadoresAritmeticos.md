# 💥 Lista de operadores Aritmeticos 💥

- ## Suma = +
- ## Resta = -
- ## Multiplicacion = *
- ## Division = /
- ## Modulo = % (Resto de la division)
- ## Exponenciacion = **
- ## Division Entera = // (Solo la parte entera de la division)

### Suma

```python
operador_1 = 10
operador_2 = 3
suma = operador_1 + operador_2
print ("el resultado de la suma es: ", suma)
print(f"el resultado de la suma es: {suma}")
```

---

### Resta

```python
operador_1 = 10
operador_2 = 3
resta = operador_1 - operador_2
print ("el resultado de la resta es: ", resta)
```

---

### Multiplicacion

```python
operador_1 = 10
operador_2 = 3
multiplica = operador_1 _ operador_2
print ("el resultado de la resta es: ", multiplica)
```

---

### Division

```python
operador_1 = 10
operador_2 = 3
divide = operador_1 / operador_2
print ("el resultado de la division es: ", divide)
```

---

### Division sin punto flotante (solo parte entera)

```python
operador_1 = 10
operador_2 = 3
divide = operador_1 // operador_2
print ("el resultado de la division es: ", divide)
```

---

### Modulo = % (Resto o residuo de la division)

```python
operador_1 = 10
operador_2 = 2
restodivision = operador_1 % operador_2
print ("el resultado del resto de la division es : ", restodivision)
```

---

### Exponenciacion = \*\*

```python
operador_1 = 10
operador_2 = 2
exponenciacion = operador_1 ** operador_2
print ("el resultado de la exponenciacion es : ", exponenciacion)
```

---

# OPERADORES de Asignacion

###  ( = ) Asignacion (el igual es el operador de asignacion)

```python
miVariable = 10
```

###  ( += ) Incremento

```python
miVariable = miVariable + 1 #Incremento
miVariable += 1 #Incremento (otra forma)
```

### -= Decremento

```python
miVariable = miVariable - 1 #Decremento
miVariable -= 1 #Decremento (otra forma)
```

### *= Multiplicacion

```python
miVariable = miVariable * 2 #Multiplicacion
miVariable *=  2 #Multiplicacion (otra forma)
```

### /= Division

```python
miVariable = miVariable / 2 #division
miVariable /= 2 #division (otra forma)
```

### %= Modulo

```python
miVariable = miVariable % 2 #Modulo
miVariable %= 2 #Modulo (otra forma)
```
### **= Exponenciacion

```python
miVariable = miVariable ** 2 #Exponenciacion
miVariable **= 2 #Exponenciacion (otra forma)
```

### //= Division Entera

```python
miVariable = miVariable // 2 #Division Entera
miVariable //= 2 #Division Entera (otra forma)
```

## Operadores de comparación

### Nos permite saber si los valores son igual o distintos, mayores o menores que otros. Los operadores de comparación son los siguientes:

### == (igualdad)

```python
a = 4
b = 2
resultado = (a == b) #Igualdad
print (f"el resultado es: {resultado}")
```
### != (desigualdad)

```python
a = 4
b = 2
resultado = (a != b) #Distintos
print (f"el resultado es: {resultado}")
```

### > (mayor)

```python
a = 4
b = 2
resultado = (a > b) #Mayor que
print (f"el resultado es: {resultado}")
```

### < (menor)

```python
a = 4
b = 2
resultado = (a < b) #Menor que
print (f"el resultado es: {resultado}")
```

### >=  (mayor o igual)

```python
a = 4
b = 2
resultado = (a >= b) #Mayor o igual que
print (f"el resultado es: {resultado}")
```

### <=  (menor o igual)

```python
a = 4
b = 2
resultado = (a <= b) #Menor o igual que
print (f"el resultado es: {resultado}")
```
---

## Operadores lógicos

### AND (y): devuelve True si ambos valores son verdaderos
```python
#Ejemplo de AND
a = True
b = True
resultado = (a and b)
print (f"el resultado es: {resultado}")
```
### OR (o): devuelve True si al menos uno de los valores es verdadero
```python
#Ejemplo de OR
a = True
b = False
resultado = (a or b)
print (f"el resultado es: {resultado}")
```
### NOT (no): devuelve True si el valor es falso

```python
#Ejemplo de NOT
a = True
resultado = (not a)
print (f"el resultado es: {resultado}")
```
### XOR (o exclusivo): devuelve True si solo uno de los valores es verdadero

```python
#Ejemplo de XOR
a = True
b = False
resultado = (a ^ b)
print (f"el resultado es: {resultado}")
```

---
## Sentencia If y Else

#### Las sentencias de control son estructuras en programación que permiten modificar el flujo de ejecución de un programa. Estas sentencias permiten tomar decisiones, ejecutar bloques de código de manera condicional o repetir ciertas operaciones mientras se cumpla una condición.

```python
a = 1
b = 2
if a > b:
  print ("a es mayor que b")
else:
  print ("a no es mayor que b")
```
---

## Comentarios en Python

### El codigo comentado en Python es ignorado por el interpretador. Esto puede ser útil para documentar el código y hacerlo más entendible.

## Almohadilla (#)

### El caracter # en Python se utiliza para comentar el resto de la línea, a partir de la misma el interpretador no procesará el código.

## Triple Comillas (""")

### En Python podemos usar las triples comillas (""")  para comentar varios renglones. Se debe usar al comienzo y al final del bloque de código que se desea comentar.

```python
# Este es un comentario en Python
print("Hola Mundo") # no es necesario comentar desde el comienzo de la línea.
"""Tambien se puede usar para 
comentar en varios renglones"""
```

## Interpolacion de cadenas
### Poniendo "f" antes de la cadena, nos permite concatenar un texto con la variable que se encuentra entre llaves.


```python
exponenciacion = 10**2
print(f"El resultado de la exponenciación es: {exponenciacion}")
```
---

# Actividades 💬

# Ejercicios - 1

- 1-Se solicita realizar un programa para mostrar el resultado de la division de dos números enteros
- 2-Se solicita realizar un programa para calcular el residuo de la division de dos números enteros
- 3-Se solicita realizar un programa para calcular el area y el perimetro de un rectangulo, para ello

  - debera crear las siguiente variables:
  - Alto (int)
  - Ancho (int)

  > El usuario debera proporcionar los valores de largo y ancho y despues imprimiro el resultado del area y el perimetro:
  > Recuerde la formula Area = largo \_ ancho // Perimetro = (largo + ancho) \* 2

# Ejercicios - 2

> 1-Se solicita realizar un programa para mostrar su el numero ingresado es par o impar (Usando operadores logicos)
> #recuerde utilizar el % para saber si es par o impar

> 2-Se solicita realizar un programa para mostrar el resultado de la division de dos números enteros

> 3-Se solicita realizar un programa para mostrar si el numero es positivo o negativo

> 4-Se solicita realizar un programa que pida la edad de una persona y determine si es mayor o menor de edad (18)

# Ejercicios - 3

- Dado un numero determine si es se encuentra entre 0 y 10

```
valor = int(input("Ingrese un numero: "))
valorMinimo = 0
valorMaximo = 10
rango = (valor >= valorMinimo) and (valor <= valorMaximo)

if rango:
  print(f"El valor: {valor} se encuentra entre 0 y 10")
else:
  print(f"El valor: {valor} no se encuentra entre 0 y 10")
```

# Ejercicios - 4

> Crear un programa que permita saber si un padre puede ir a ver como juega su hijo dependiendo si es un dia de descanso o si esta de vacaciones (usar operadores logicos)- de lo contrario no puede ir.

> Ejemplo NOT (mismo ejercicio pero invierta el resultado)

> Crear un programa que permita al usuario ingresar su edad y determine si esta entre los 20 (de 20 a 30 años) y los 40 años(de 40 a 50 años) .

> crear un progrmaa que permita que usuario ingrese dos numeros enteeros y nos imprima cual es el mayor de los dos numeros ingresados
> (#ver DEBUGGER)

> TIENDA DE LIBROS: Crear un programa que permita ingresar un libro y su autor, muestre el precio (float) y deje escribir si el envio es gratis(true o false)

# Para imprimir toda la info utilizar el print

```python
print (f'''
Hola mundo, aca se puede imprimir
respetando los enter y los tabluladores.
''')
libro = input('Ingrese el nombre del libro:')
autor = input('Ingrese el nombre del autor:')
precio = float(input('Ingrese el precio:'))
envioGratis = input('¿El envio es gratis?/("SI") o ("NO")')

if envioGratis != "SI" and envioGratis != "NO":
   envioGratis="SI"
  print (f'''
  Libro : {libro}
  Auto : {autor}
  Precio : {precio}
  envio es gratis: {envioGratis}
''')
```

---

[VOLVER](/pythonCurso/readme.md)

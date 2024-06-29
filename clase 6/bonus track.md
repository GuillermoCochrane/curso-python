# Bonus track: 

## Trivia 1: 
### Dado el siguiente código:

```python
a = 20 
b = 19
c = 22

mensaje_true = "a es mayor a b y b es  menor a c"
mensaje_false = "esto no se cumple"

if a >b and b<c :
     print(mensaje_true)
else:
     print (mensaje_false)
```
- Se imprime la variable: mensaje_true
- Se imprime la variable: mensaje_false

---

## Ejercicio 1

> Realizar un programa que permita el ingreso de 4 personas con su nombre y apellido, su dirección y la edad y muestre en pantalla cual es la persona(con todos los datos ingresados) ,  con mayor edad (y en que posición se cargo) y la de menor edad y en que posición se cargo (Por ejemplo Diego Markiewicz de 44 años, vive en General Levalle y  fue cargado en el registro número 3 y Robb Stark de 28 años vive en Winterfell y fue cargado en el registro número 1)

```python
#solucion clase 1
```

```python
#solucion clase 2
```
---

## Ejercicio 2

> Realizar un programa que me permita ingresar tres valores, siendo los primeros dos los números a utilizar y el tercero indicará la operación matemática a realizar(S, R, M, D) necesitaría que cuando me imprima el resultado tenga el siguiente formato de salida: 
> Operación realizada con éxito, el resultado de (Aquí debe mostrar que operación se realizó) es (aquí debe mostrar el resultado) tengan en cuenta que no se puede dividir por CERO así que me debería advertir si lo coloco en el segundo número

```python
#solucion clase 1
```

```python
#solucion clase 2
```
---

## Ejercicio 3
> Realizar un programa que me diga si el número ingresado es par o impar

```python
#solucion
```

---

## Ejercicio 4

> Realizar un juego donde la computadora seleccione un numero aleatorio del 1 al 10 y nosotros como jugadores tengamos hasta tres oportunidades de adivinar el numero, si ganamos que nos muestre un mensaje felicitándonos y mostrando el numero aleatorio seleccionado. Tener en cuenta que el numero seleccionado por la computadora al inicio es el mismo que deben evaluar en los tres intentos!. El programa deberá mostrar en que numero de intento lo acerte. Tambien deberá mostrar un mensaje como un "Frio" cuando estoy mas alla de 3 numeros o "Caliente" cuando estoy a menos de 3.


```python
#solucion clase 1
```

```python
#solucion clase 2
```
---

## Ejercicio 5
> Realizar un juego de piedra, papel y tijera donde el usuario.

```python
#solucion
```  
---

## Trivia 2: 
### Dado el siguiente código, quiero saber si es Verdadero decir que el envío va a ser "gratis" si escribo algo distinto a SI o a NO

```python
libro = input('Ingrese el nombre del libro:')
autor= input('Ingrese el nombre del autor:') precio = float(input('Ingrese el precio:'))
envioGratis = input('¿El envio es gratis?/("SI") o ("NO")').upper()
if envioGratis != "SI" and envioGratis != "NO":
     envioGratis="SI"
print (f'''Libro: {libro}
Auto: {autor}
Precio: {precio}
¿Envio gratis?: {envioGratis}
''')

```
- verdadero
- falso
---
hasta 31/5/2024
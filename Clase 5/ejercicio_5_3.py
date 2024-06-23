#Se solicita realizar un programa para calcular el area y el perimetro de un rectangulo, para ello debera crear las siguiente variables: 
#Alto (int), Ancho (int)
#El usuario debera proporcionar los valores de largo y ancho y despues imprimiro el resultado del area y el perimetro:
#Area: alto * ancho
#Perimetro: (alto + ancho) * 2

alto = int(input("Ingrese el alto de la rectangulo: "))
ancho = int(input("Ingrese el ancho de la rectangulo: "))

area = alto * ancho
perimetro = (alto + ancho) * 2

print("El area de la rectangulo es: ", area)
print("El perimetro de la rectangulo es: ", perimetro)
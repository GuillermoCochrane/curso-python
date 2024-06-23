# TIENDA DE LIBROS: 
# Crear un programa que permita ingresar un libro y su autor, muestre el precio (float) y deje escribir si el envio es gratis(true o false)

libro = input("Ingrese el nombre del libro: ")
autor = input("Ingrese el nombre del autor: ")
precio = float(input("Ingrese el precio: "))
envioGratis = input("¿El envio es gratis? ")
envio = False
if envioGratis == "SI":
    envio = True

print("\n")
print("Libro:", libro)
print("Autor:", autor)
print(f"Precio: ${precio}")
if envio:
    print("El envio es gratis")
else:
    print("El envio no es gratis")
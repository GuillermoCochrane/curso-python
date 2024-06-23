# Escribir 3 variables para que guarden Apellido y nombre - Email y telefono y mostrarlos en pantalla, con el siguiente mensaje "Hola, Mi nombre es: ..., te paso mi contacto telefonico: ... y mi email: ..."

#-Pedirle al usuario que ponga como estuvo su dia (del 1 al 10) y luego mostrar el texto "Mi dia estuvo de: " y el valor ingresado
#-Pedir al usuario que ingrese su edad y su ciudad de residencia, y luego mostrar estos datos en una frase.
#-Solicitar al usuario que ingrese su comida favorita y su bebida favorita, luego mostrar un mensaje que contenga ambas respuestas.

nombreApellido = "Walter White"
telefono = "+1 (505) 555-0199"
mail = "walter.white@jpwynnehs.edu";

print("Hola, mi nombre es", nombreApellido, "y te paso mi contacto telefonico", telefono, "y mi email", mail)

dia = int(input("¿Como estuvo de su día? "))
print(f"Mi día estuvo de {dia}")

edad = int(input("¿Cuántos años tiene? "))
ciudad = input("¿Cuál es tu ciudad de residencia? ")
print(f"Mi edad es {edad} y vivo en {ciudad}")

comida = input("Cual es tu comida favorita? ")
bebida = input("Cual es tu bebida favorita? ")
print(f"Mi comida favorita es {comida} y mi bebida favorita es {bebida}")
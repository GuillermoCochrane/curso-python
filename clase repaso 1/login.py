lista_usuarios = [
    {
        "nombre": "Jon",
        "password": "promised_Prince",
    },
    {
        "nombre": "Robb",
        "password": "Young#wolf16",
    },
    {
        "nombre": "Tyrion",
        "password": "the$Imp69",
    }
]
contador_usuario = 5
contador_password = 5

while True:
    print("\n¡Bienvenido!")
    nombre = input("Ingrese su nombre de usuario: ")
    usuario_encontrado = False

    for usuario in lista_usuarios:        
        if usuario["nombre"] == nombre:
            password_guardado = usuario["password"]
            usuario_encontrado = True

            while True:
                password = input("Ingrese su contraseña: ")
                if password == password_guardado:
                    exit("\n¡Bienvenido " + nombre + "!")
                else:
                    contador_password -= 1
                    if contador_password == 0:
                        exit("¡No le quedan más intentos!")
                    print(f"Contraseña incorrecta, le quedan {contador_password} intentos\n")

    if not usuario_encontrado:
        contador_usuario -= 1
        if contador_usuario == 0:
            exit("¡No le quedan más intentos!")
        print(f"Usuario no encontrado, le quedan {contador_usuario} intentos")
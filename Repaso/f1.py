#Crea una funcion que nos salude por consola

def saludar(nombre: str | None = ", debe ingresar su nombre. "):
    print(f"Hola {nombre}")
    
saludar()
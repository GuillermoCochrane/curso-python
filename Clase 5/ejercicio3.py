# Se solicita incluir la siguiente informacion acerca de un libro : Título, autor, número de páginas, año de publicación.
# Se pide que el usuario ingrese la información solicitada de la siguiente manera:.

# - Ingrese el Titlo del libro :
# - Ingrese el Autor :
# - Ingrese el Numero de Paginas :
# - Ingrese el Año de publicación :
# - Imprimir : " El Libro `<nombre del libro>` fue escrito por `<autor>` y tiene `<numero de paginas>` paginas, y fue publicado en el año `<año de publicacion>`"

titulo = input("Ingrese el titulo del libro: ")
autor = input("Ingrese el autor del libro: ")
paginas = input("Ingrese el numero de paginas del libro: ")
anio = input("Ingrese el año de publicacion del libro: ")

print(f"El libro {titulo} fue escrito por {autor} y tiene {paginas} paginas, y fue publicado en el año {anio}")
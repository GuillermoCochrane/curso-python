import tkinter as tk
from PIL import ImageGrab  # pip install pillow
from tkinter import filedialog

def borrar_linezo():
    linezo.delete("all")

def cambiar_color_pincel(color):
    color_pincel.set(color)

def guardar():
    x0 = linezo.winfo_rootx()
    y0 = linezo.winfo_rooty()
    x1 = x0 + linezo.winfo_width()
    y1 = y0 + linezo.winfo_height()
    img = ImageGrab.grab(bbox=(x0, y0, x1, y1))
    archivo = filedialog.asksaveasfilename(defaultextension=".png")
    if archivo:
        img.save(archivo)

x_anterior = None
y_anterior = None

def dibujar__inicio(evento):
    global x_anterior, y_anterior
    x_anterior = evento.x
    y_anterior = evento.y

def dibujar(evento):
    global x_anterior, y_anterior
    linezo.create_line(x_anterior, y_anterior, evento.x, evento.y, fill=color_pincel.get(), width=2)
    x_anterior = evento.x
    y_anterior = evento.y

ventana = tk.Tk()
ventana.title("Paint Oficial UPGL")
ventana.geometry("500x500")

# Menú superior
menu_bar = tk.Menu(ventana)

option_menu = tk.Menu(menu_bar, tearoff=0)
color_menu = tk.Menu(option_menu, tearoff=0)

option_menu.add_command(label="Borrar", command=borrar_linezo)
option_menu.add_command(label="Guardar", command=guardar)

# Lista de colores
colores = [
    {"color": "black", "nombre": "negro"},
    {"color": "green", "nombre": "verde"},
    {"color": "orange", "nombre": "naranja"},
    {"color": "purple", "nombre": "púrpura"},
    {"color": "red", "nombre": "rojo"},
    {"color": "blue", "nombre": "azul"},
    {"color": "yellow", "nombre": "amarillo"},
    {"color": "cyan", "nombre": "cian"},
    {"color": "magenta", "nombre": "magenta"},
    {"color": "white", "nombre": "blanco"},
    {"color": "goldenrod", "nombre": "dorado"}
]

# Creación del menú de colores
for color in colores:
    color_menu.add_command(label=color["nombre"], command=lambda c=color["color"]: cambiar_color_pincel(c))

menu_bar.add_cascade(label="Opciones", menu=option_menu)
menu_bar.add_cascade(label="Color", menu=color_menu)

ventana.config(menu=menu_bar)

color_pincel = tk.StringVar()
color_pincel.set("#ebebeb")

linezo = tk.Canvas(ventana, width=400, height=400, background="#999999")
linezo.pack()

linezo.bind("<B1-Motion>", dibujar)
linezo.bind("<Button-1>", dibujar__inicio)

ventana.mainloop()

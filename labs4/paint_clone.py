import tkinter as tk

def borrar_linezo():
    linezo.delete("all")

def cambiar_color_pincel(color):
    print(color)
    color_pincel.set(color)

def seleccionar_color_rojo():
    cambiar_color_pincel("red")
    
def seleccionar_color_negro():
    cambiar_color_pincel("black")
    
def seleccionar_color_verde():
    cambiar_color_pincel("green")

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

boton_negro = tk.Button(ventana, text="Negro", command=seleccionar_color_negro, background="#444444", fg="#ebebeb", )
boton_negro.pack()

boton_rojo = tk.Button(ventana, text="Rojo", command=seleccionar_color_rojo, background="#ff0000", fg="#ebebeb", )
boton_rojo.pack()

boton_verde = tk.Button(ventana, text="Verde", command=seleccionar_color_verde, background="green", fg="#333333", )
boton_verde.pack()

color_pincel = tk.StringVar()
color_pincel.set("#ebebeb")

linezo =tk.Canvas(ventana, width=400, height=400, background="#999999")
linezo.pack()

linezo.bind("<B1-Motion>", dibujar)
linezo.bind("<Button-1>", dibujar__inicio)

boton_borrar = tk.Button(ventana, text="Borrar", command=borrar_linezo, background="tomato", fg="#ebebeb" )
boton_borrar.pack()

ventana.mainloop()
#Funcion para validar edad

import datetime

def calcular_edad(fecha_nacimiento):
    fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, '%d/%m/%Y')
    hoy = datetime.date.today()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

#fecha_nacimiento = "01/01/2000"
#edad = calcular_edad(fecha_nacimiento)
#print(f"Mi edad es {edad}")
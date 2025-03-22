
from datetime import *

def dias_para_2026():
    ahora = datetime.now()
    return anio_2026 - ahora

def print_date(date):
    print(date.strftime("%d/%m/%Y"))

ahora = datetime.now()
print(ahora)
print(ahora.day)
print(ahora.month)
print(ahora.year)
print(ahora.second)
print(type(ahora))

timestamp = ahora.timestamp()
print(timestamp) #es como un formato de fecha en segundos estandard

fecha = datetime.fromtimestamp(timestamp)
print(fecha) #ahora se convierte de nuevo a fecha normal

un_anio_dias = timedelta(days=365)

#fecha completa de el inicio de un año
anio_2026 = datetime(2026, 1, 1)
print(anio_2026)
print_date(anio_2026)

#print(dias_para_2026())

#solo hora
momento = time( 12,30,20)
print(momento)

#solo fecha
fecha = date(2020, 12, 31)
print(fecha)

#operaciones con fechas
print(fecha + timedelta(days=1)) #sumar un dia
print(fecha - timedelta(days=1)) #restar un dia
print(fecha + timedelta(days=365)) #sumar un año
print(fecha + timedelta(days=365*4)) #sumar 4 años
print(fecha + timedelta(days=365*4+1)) #sumar 4 años y un dia
print(fecha + timedelta(days=365*4-1)) #sumar 4 años menos un dia
print(fecha + timedelta(days=365*4+365)) #sumar 4 años y un año
print(fecha + timedelta(days=365*4-365)) #sumar 4 años menos un año
print(fecha + timedelta(days=365*4+366)) #sumar 4 años y un año bisiesto
print(fecha + timedelta(days=365*4-366)) #sumar 4 años menos un año bisiesto
print(fecha + timedelta(days=365*4+365+1)) #sumar 4 años y un año y un dia
print(fecha + timedelta(days=365*4-365-1)) #sumar 4 años menos un año y un dia


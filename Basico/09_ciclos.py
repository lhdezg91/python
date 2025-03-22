### Ciclos ####

# while

condicion = 0

while(condicion < 10):
    print(condicion)
    condicion += 1
else: #Es opcional
    print("Fin del ciclo while")


# for

for i in range(10):
    print(i)
    if i == 5:
        break

list = ["lian","ivis","leanny","lianet",5,6,7,8,9,10]

# imprimir los elementos de la lista
for i in list:
    print(i)
    if i == 5:
        continue
    print("No se ejecuta si i es igual a 5")





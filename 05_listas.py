### LISTAS ###

my_list = [1, 2, 3, "ian", 5]
print(my_list)

list = list()
otra_lista = []

print(my_list[0]) # 1

list.append(6)
list.append(67)
list.append(8)
list.append("ian")
list.append("ok")

list.insert(2, "hola") # insertar en la posicion 3

list.remove(67) # remover si hay varios elimina el primero

list.pop() # elimina el ultimo

elemento = list.pop(2) # elimina el elemento en la posicion 2, devuelve el elemento eliminado

del list[0] # elimina el elemento en la posicion 0

print(list[-1]) # de atras para alante

print(list.count("ian")) # cuantas veces aparece


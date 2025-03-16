### Tuplas ###
# Las tuplas son una secuencia de elementos que no pueden ser modificados
my_tuple = tuple()
my_tuple = ()
my_tuple = (1,2,3,"ian",5)
print(my_tuple)
print(my_tuple[0]) # 1 

my_tuple.index("ian") # 3 dice en que posicion esta

# my_tuple[1] = 3 # error no se puede modificar

my_list = list(my_tuple) # convierte a lista

def suma_uno(n):
    return n + 1

def suma_cincos(n):
    return n + 5

# Función que recibe dos valores y una función
def suma_dos_valores_mas_otro(valor1, valor2, valor3):
    return valor3(valor1 + valor2)

print(suma_dos_valores_mas_otro(1, 2, suma_uno))
print(suma_dos_valores_mas_otro(1, 2, suma_cincos))


### Closure ###

def suma_x(x):
    def suma(n):
        return n + x
    return suma

suma_cinco = suma_x(5)
print(suma_cinco(10)) # 15

### Funciones del Sistema ###
# map
numeros = [1, 2, 3, 4, 5]
map(suma_uno, numeros)
print(list(map(suma_uno, numeros))) # [2, 3, 4, 5, 6]
print(list(map(lambda number: number +1 , numeros))) # [2, 3, 4, 5, 6]


# filter
def es_par(n):
    return n % 2 == 0

print(list(filter(es_par, numeros))) # [2, 4]
print(list(filter(lambda number: number % 2 == 0, numeros))) # [2, 4]

# reduce

from functools import reduce

def suma(a, b):
    return a + b

print(reduce(suma, numeros)) # 15
print(reduce(lambda a, b: a + b, numeros)) # 15



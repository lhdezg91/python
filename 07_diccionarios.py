### Diccionarios ###
# Son estructuras de datos que permiten almacenar multiples valores, como listas, pero en lugar de usar
# Un indice para acceder a los valores se usan claves.
# Un diccionario se crea con llaves {} y los elementos se separan con comas.
# Cada elemento del diccionario es una pareja clave:valor.
# Las claves son unicas y no pueden repetirse.
# Los valores pueden ser de cualquier tipo.
# Los diccionarios son mutables, es decir, se pueden modificar.
# Los diccionarios no tienen orden.
# Los diccionarios son iterables.
# Los diccionarios pueden contener otros diccionarios.
# Los diccionarios pueden contener listas.
# Los diccionarios pueden contener tuplas.
# Los diccionarios pueden contener sets.
# Los diccionarios pueden contener funciones.
# Los diccionarios pueden contener clases.
# Los diccionarios pueden contener objetos.
# Los diccionarios pueden contener modulos.
# Los diccionarios pueden contener cualquier cosa.
#
# Crear un diccionario  vacio
my_dict = dict()
my_dict = {}    # forma mas comun

# Crear un diccionario con elementos
my_dict = {"nombre":"ian","edad":30,"ciudad":"lima"}
print(my_dict)

# Acceder a un elemento
print(my_dict["nombre"]) # ian

# Modificar un elemento
my_dict["nombre"] = "juan"
print(my_dict)

# Agregar un elemento
my_dict["sexo"] = "masculino"
print(my_dict)

# Eliminar un elemento
del my_dict["sexo"]
print(my_dict)

# Obtener la longitud
print(len(my_dict))

# Eliminar todos los elementos
my_dict.clear()
print(my_dict)

# Eliminar el diccionario
del my_dict
# print(my_dict) # error porque ya no
# existe el diccionario

# Diccionarios anidados
my_dict = {
    "persona1": {"nombre":"ian","edad":30},
    "persona2": {"nombre":"juan","edad":40}
}
print(my_dict)

# Diccionarios con listas
my_dict = {
    "persona1": ["ian",30],
    "persona2": ["juan",40]
}
print(my_dict)

# Diccionarios con tuplas
my_dict = {
    "persona1": ("ian",30),
    "persona2": ("juan",40)
}
print(my_dict)

# Diccionarios con sets
my_dict = {
    "persona1": {"ian",30},
    "persona2": {"juan",40}
}
print(my_dict)

# Diccionarios con funciones
def saludo():
    return "hola"

my_dict = {
    "saludo": saludo
}
print(my_dict["saludo"]())

# Diccionarios con clases
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return f"{self.nombre} {self.edad}"

persona1 = Persona("ian",30)
persona2 = Persona("juan",40)   

my_dict = {
    "persona1": persona1,
    "persona2": persona2
}
print(my_dict["persona1"])

# Diccionarios con objetos
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return f"{self.nombre} {self.edad}"

persona1 = Persona("ian",30)
persona2 = Persona("juan",40)

my_dict = {
    "persona1": persona1,
    "persona2": persona2
}
print(my_dict["persona1"])

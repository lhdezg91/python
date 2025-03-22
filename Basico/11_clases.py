### Clases ###

class Persona:
    def __init__(self, nombre, edad): # Constructor
        self.nombre = nombre # Atributo publico
        self.__edad = edad # Atributo privado
    
    def get_edad(self):
        return self.__edad

    def saludar(self):
        print(f'Hola, mi nombre es {self.nombre} y tengo {self.__edad} años')


# Instanciar la clase
persona1 = Persona("lian", 30)
print(persona1.nombre)
persona1.saludar()
persona1.nombre = "Ivis"
print(persona1.get_edad())
#persona1.__edad = 31 # No se puede modificar un atributo privado
persona1.saludar()
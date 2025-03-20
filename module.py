
class Persona:
    def __init__(self, nombre, edad): # Constructor
        self.nombre = nombre # Atributo publico
        self.__edad = edad # Atributo privado
    
    def get_edad(self):
        return self.__edad

    def saludar(self):
        print(f'Hola, mi nombre es {self.nombre} y tengo {self.__edad} años')
        
def suma(a, b):
    print(a + b) 
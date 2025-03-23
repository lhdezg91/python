def reto1():
    # https://www.python.org/
    """
    Reto 1: Imprimir un mensaje en pantalla
    """
    texto = "Python"
    numero = 10
    booleano = True
    flotante = 10.5
    
    print(f"!Hola, {texto}!!")

class Reto2:
    def __init__(self, texto1, texto2):
        self.texto1 = texto1
        self.texto2 = texto2
        
    def imprimir(self):
        contador = 0
        for i in range(1, 101):
            
            if i % 3 == 0 and i % 5 == 0:
                print(f"{self.texto1} {self.texto2}")                            
            elif i % 3 == 0:
                print(f"{self.texto1}")            
            elif i % 5 == 0:
                print(f"{self.texto2}")            
            else :
                print(i)                     
                contador += 1
            
        return contador

class Agenda:
    def __init__(self):
        self.contactos = []
        
    def agregar_contacto(self, nombre, telefono):
        if telefono.isdigit() or len(telefono) > 11:
            print("El telefono debe ser un numero menor a 11 digitos")
            return
        
        self.contactos.append((nombre, telefono))
        
    def mostrar_contactos(self):
        for contacto in self.contactos:
            print(contacto)
            
    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto[0] == nombre:
                print(contacto)
                return contacto
            
        print("Contacto no encontrado")
        return None
    
    def eliminar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto[0] == nombre:
                self.contactos.remove(contacto)
                print("Contacto eliminado")
                return contacto
            
        print("Contacto no encontrado")
        return None

"""
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
"""
def es_anagrama(palabra1, palabra2):
    #return sorted(palabra1) == sorted(palabra2)
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    
    if len(palabra1) != len(palabra2):
        return False
    if palabra1 == palabra2:
        return False
    
    for i in palabra1:
        if i not in palabra2:
            return False
    
    return True

"""
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */
"""

def fibonacci():
    a, b = 0, 1
    for i in range(50):
        print(a)
        a, b = b, a + b

def es_primo(num):
    if num < 2:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def invertir(cadena):
    cadena2 = ""
    for i in range(1, len(cadena)+1):
        cadena2 = cadena2 + cadena[-i]
    print(cadena2)

invertir("hola")

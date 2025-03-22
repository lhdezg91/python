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
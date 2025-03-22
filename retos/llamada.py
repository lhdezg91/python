from retos import *

#reto1
print(type(34))
reto1()

#reto2
var = Reto2("Python", "Java").imprimir()
print(var)


#reto3
agenda = Agenda()
salir = False
while salir==False:
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    opcion = input("Ingrese una opcion: ")
    
    if opcion == "1":
        nombre = input("Ingrese el nombre: ")
        telefono = input("Ingrese el telefono: ")
        agenda.agregar_contacto(nombre, telefono)
    elif opcion == "2":
        agenda.mostrar_contactos()
    elif opcion == "3":
        nombre = input("Ingrese el nombre: ")
        agenda.buscar_contacto(nombre)
    elif opcion == "4":
        nombre = input("Ingrese el nombre: ")
        agenda.eliminar_contacto(nombre)
    elif opcion == "5":
        salir = True
    else:
        print("Opcion no valida")

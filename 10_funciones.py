### Funciones ###

def mi_funcion():
    print("Hola mundo")

def suma_funcion(primer_numero, segundo_numero):
    #print(primer_numero + segundo_numero)
    return primer_numero + segundo_numero

def fullname(nombre,apellido):
    return f"{nombre} {apellido}"

#alias por defecto, si no se pasa un valor se asigna el valor por defecto
def fullname_alias(nombre,apellido, alias = "No tiene"):
    return f"{nombre} {apellido} {alias}"

def imprimir_textos_dinamicos(*args):
    for texto in args:
        print(texto)



#las funciones tienen que declararse antes de ser llamadas

mi_funcion()

primero = 5
suma = suma_funcion(primero,1)
print(suma)

print(fullname("lian","hernandez"))

print(fullname_alias("lian","hernandez"))

imprimir_textos_dinamicos("lian","hernandez","ivis","leanny","lianet")
imprimir_textos_dinamicos("lian","hernandez","ivis","leanny","lianet","ivan","luis","luisa","luisana","luisito")
imprimir_textos_dinamicos("lian","hernandez","ivis")



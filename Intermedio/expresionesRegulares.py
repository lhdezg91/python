
import re

texto = "Esta es una Cadena de texto y cadena de texto numero 1"

texto2 = "texto"



match = re.match("Esta es una",texto)#busca desde el principio
print(re.match("es una cadena",texto, re.I))#IgnoreCase
#match = re.match("es una cadena",texto, re.I)#IgnoreCase

if match != None:
    print(match.span())
    inicio, fin = match.span()
    print(texto[inicio:fin])

# buscar

print(re.search("cadena",texto))
match = re.search("cadena",texto)

if match.span == None:
    print("No contiene la cadena")
else:
    print("Contiene la cadena")

# findall

print(re.findall("cadena",texto))
match = re.findall("cadena",texto)
match = re.findall("cadena",texto, re.I)#Si le ponemos el ignorecase no importan las mayusculas

print(len(match))

if len(match) == 0:
    print("No contiene la cadena")
else:
    print(match)

#split

print(re.split("y", texto))

#sub

print(re.sub("texto", "TEXTO", texto))
print(re.sub("cadena|Cadena", "CADENA", texto))
print(re.sub("[c|C]adena", "CADENA", texto))

#patrones

patron = r"[c|C]adena"

print(re.findall(patron,texto))

patron = r"[c|C]adena|texto"

print(re.findall(patron,texto))

patron = r"[0-9]"

print(re.findall(patron,texto))


# Patrón de expresión regular para correos electrónicos
email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Ejemplo de validación
def validar_email(email):
    return bool(re.match(email_regex, email))

# Prueba
email = "ejemplo@dominio.com"
if validar_email(email):
    print("El correo es válido")
else:
    print("El correo no es válido")
    





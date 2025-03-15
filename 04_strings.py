#salto de linea
print("hola\nmundo")

#tabulador
print("hola\tmundo")

#comillas
print("\"hola mundo\"") #comillas do
print('\'hola mundo\'') #comillas simples   

#concatenar
print("hola" + " " + "mundo")

#repetir
print("hola "*3)    

#mayusculas
print("hola mundo".upper()) #mayusculas

#minusculas
print("HOLA MUNDO".lower()) #minusculas

#capitalizar
print("hola mundo".capitalize()) #capitalizar

#reemplazar
print("hola mundo".replace("mundo","python")) #reemplazar

#buscar
print("hola mundo".find("mundo")) #buscar

#contar
print("hola mundo".count("o")) #contar  

#comparar
print("hola mundo" == "hola mundo") #comparar   

print("hola mi nombre es {} y mi edades es {}".format("juan",30)) #format
print("hola mi nombre es %s y mi edades es %d" %("juan",30)) #format
nombre = "juan"
edad = 30
print(f"hola mi nombre es {nombre} y mi edades es {edad}")
### Modules ###

from module import Persona # Importar la clase Persona del modulo module

Persona1 = Persona("lian", 30)
print(Persona1.nombre)
Persona1.saludar()

from module import suma # Importar la funcion suma del modulo module
suma(5, 5)

from module import * # Importar todo del modulo module
Persona2 = Persona("Ivis", 31)
print(Persona2.nombre)
Persona2.saludar()
suma(10, 10)

# Importar un modulo con un alias
import module as m
Persona3 = m.Persona("Lian", 32)
print(Persona3.nombre)
Persona3.saludar()
m.suma(15, 15)

# Importar solo una funcion de un modulo
from module import suma as s
s(20, 20)

# Importar solo una clase de un modulo
from module import Persona as P
Persona4 = P("Ivis", 33)
print(Persona4.nombre)
Persona4.saludar()
#suma(25, 25) # No se puede porque no se importo la funcion suma

# Importar un modulo de la libreria estandar
import math, random
print(math.pi)
print(random.randint(1, 10))

# Importar un modulo de la libreria estandar con un alias
import math as m
print(m.pi)

# Importar solo una funcion de un modulo de la libreria estandar
from math import pi
print(pi)

# Importar todo de un modulo de la libreria estandar
from math import *
print(pi)
print(e)

# Importar un modulo de un paquete
from package.module import Persona as P
Persona5 = P("Lian", 34)    
print(Persona5.nombre)
Persona5.saludar()

from package.module import suma as s
s(30, 30)

# Importar un modulo de un paquete con un alias
from package import module as m
Persona6 = m.Persona("Ivis", 35)
print(Persona6.nombre)
Persona6.saludar()

from package.module import suma as s
s(35, 35)

# Importar todo de un modulo de un paquete
from package.module import *


# Manera de importar la clase
from clasesYobjetos import Persona

print("Creacion de objetos".center(50,"-"))

persona1=Persona("Juan","Martinez",19)

persona1.mostrar_detalles()

print("Eliminacion de objeto".center(50,"-"))
del persona1



from Manejos_de_los_archivos import ManejoArchivos
# Uso de with, archivos y context manager con python

# with open("prueba.txt","r",encoding="UTF-8") as archivo:
#       print(archivo.read())      
 
with ManejoArchivos("prueba.txt") as archivo:
     print(archivo.read())














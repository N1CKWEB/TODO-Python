# Test de polimorfismo

from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalles(objeto):
  print(objeto)
  print(type(objeto))
  
  #Si nosotros queremos preguntar si cierto objeto corresponde a una instancia de cierta clase, puedo utilizar este métdo (isinstance)    
  if isinstance(objeto, Gerente):
   print(objeto.departamento)


empleado01=Empleado("Nico",5000)

imprimir_detalles(empleado01)

gerente01=Gerente("Nicolas Ariel",15000,"De Desarrollo de IA y Robotica")

imprimir_detalles(gerente01)





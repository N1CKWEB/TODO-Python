# Sobrecarga de operadores en python

class Persona:
    def __init__(self, nombre,edad):
      self.nombre = nombre
      self.edad = edad
    
    def __add__(self,otro):
        return f"{self.nombre} {otro.nombre}"
      
    def __sub__(self,otro):
        return self.edad -  otro.edad
      
    
 
persona1=Persona("Nicolas",19)

persona2=Persona("Ariel",29) 

print(persona1+persona2)   
print(persona1-persona2)   
    


           
        







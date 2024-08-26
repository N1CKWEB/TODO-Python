

# 3 formas para representar un objeto en python

# Representación de objetos (str,repr,format)

# print(dir(object))


class Persona:
    
    def __init__(self, name, age):
      self.name = name
      self.age = age
      
    # repr(), más enfocado a los programadores   
    def __repr__(self) -> str:
        return f"{self.__class__.__name__} ( nombre = {self.name} , age = {self.age} )" 
   
    
    # str(), más orientado para el usuario final, o inclusime otros sitemas la implementación por default llama al método repr
    def __str__(self) -> str:
       return f"{self.__class__.__name__} (nombre = {self.name} , age = {self.age})  "
   
     
    #format(), su implentación por default es el método str, y se manda a llamar al usar f-string
    def __format__(self, format_spec: str) -> str:
       return   f"{self.__class__.__name__} con nombre  {self.name} y edad {self.age}"  
   
   
   
persona1=Persona("Nicolas",19)
# repr (!r)
print(f"Mi objeto persona1: {persona1!r}")
# str (de manera automatica el método print llama al método str )
print(persona1)
# format
print(f"{persona1}")










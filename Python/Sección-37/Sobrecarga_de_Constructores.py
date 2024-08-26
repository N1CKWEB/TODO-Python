

# Sobrecarga de constructores en python

# Simulación de constructores en python
# Otras forma de crear objetos
 

class Persona:
     def __init__(self, name, age):
       self.name = name
       self.age = age

     @classmethod
     def crear_persona_vacia(cls):
         return cls(None,None)

     @classmethod
     def crear_persona_con_valores(cls,nombre,apellido):
         return cls(nombre,apellido)

     
     def __str__(self) -> str:
         return f"Persona: [Nombre: {self.name} , Edad: {self.age}]"

     
     
     

persona1=Persona('Nicolas',19)
print(persona1)
persona_vacio=Persona.crear_persona_vacia()
print(persona_vacio)
persona_con_valores=Persona.crear_persona_con_valores('Mariela',49)
print(persona_con_valores)






























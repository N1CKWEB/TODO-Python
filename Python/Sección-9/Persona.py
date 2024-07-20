# Ejercicio - Contador Objetos

class Persona:
    
    contador_personas = 0
    
    #Método de clase
    @classmethod
    def _generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self,nombre,edad):
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre=nombre
        self.edad=edad
      
      
    def __str__(self) -> str:
        return f"Persona: [{self.id_persona} {self.nombre} {self.edad}]"  
    
    
    
persona01=Persona("Nico",19)
persona02=Persona("Juan",19)
persona03=Persona("Naim",19)
persona04=Persona("Gordo",19)


print(persona01)    
print(persona02)    
print(persona03)    
print(persona04)    

Persona.generar_siguiente_valor()
persona05=Persona("Juanchi",22)

print(persona05)
print(f"Valor contador personas: {Persona.contador_personas}")
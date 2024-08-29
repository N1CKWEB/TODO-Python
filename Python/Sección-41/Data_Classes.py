

# Data Classes es un modulo de python que provee decoradores y funciones y se agregan de manera automatica se agregan a nuestras clases

from dataclasses import dataclass
from typing import ClassVar

@dataclass(eq=True,frozen=True)

class Domicilio:
    
    calle:str
    numero:int
    
    

# frozen viene hacer congelado (No modificable o inmutable)
@dataclass(eq=True,frozen=True)

class Persona:
      
    nombre:str
    apellido:str 
    edad:int
    domicilio:Domicilio
    contador_personas: ClassVar[int]=0
     
    def __post_init__(self):
        if not self.nombre:
           raise ValueError(f"Valor de nombre vacio: {self.nombre}")
         
     
     
domicilio1=Domicilio("Aconcagua",3319)
persona1=Persona("Nicolas","Diaz",19,domicilio1)     

print(f"{persona1!r}")    

# Variable de clase

print(f"Variable de clase: {Persona.contador_personas}")

# Variables de instancia de nuestro objeto

print(f"Variables de instancia: {persona1.__dict__}")

# Variable con valores vacíos

persona_vacia=Persona('Sergio','Diaz',49,Domicilio("Barrio Vista Olivo Manzana J",19))

print(f"Persona vacia: {persona_vacia}")



# Revisar igualdad entre objetos (__eq__)

persona2=Persona("Nicolas","Diaz",19,Domicilio("Aconcagua",3319))
print(f"Objetos iguales?",{persona1 == persona2})

# Agregar esta clases a una colecciones

coleccion = {persona1,persona2}
print(coleccion)


# Frozen = True

# coleccion[0].nombre="Juan Carlos"
# persona1.nombre="Juan Carlos"











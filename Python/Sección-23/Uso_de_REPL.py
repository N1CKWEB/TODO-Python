
# REPL: Nos permite interactuar con el intérprete de python directamente

# Uso de REPL y tipo None en python


class Persona:
    def __init__(self, nombre, apellido):
      self.nombre = nombre
      self.apellido = apellido

    def __str__(self) -> str:
       return f"Persona: [Nombre: {self.nombre} Apellido:{self.apellido} ID: {hex(id(self)).upper()}]"



persona1=Persona("Nicolás","Díaz")

print(persona1)













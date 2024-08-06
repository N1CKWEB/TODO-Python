from Logger_base import log

class Persona:
    
    def __init__(self, id_persona=None,nombre=None,apellido=None,edad=None,email=None):
      self._id_persona = id_persona
      self._nombre = nombre
      self._apellido = apellido
      self._edad = edad
      self._email = email
      
      #GET y SET
       
      @property
      def id_persona(self):
          return self._id_persona
      
      @id_persona.setter
      def id_persona(self,id_persona):
          self._id_persona=id_persona
      
    #   @property
      def nombre(self):
          return self._nombre
      
      @nombre.setter
      def nombre(self,nombre):
          self._nombre=nombre
      
      @property
      def apellido(self):
          return self._apellido
      
      @apellido.setter
      def apellido(self,apellido):
          self._apellido=apellido
      
      @property
      def edad(self):
          return self._edad
      
      @edad.setter
      def edad(self,edad):
          self._edad=edad
      
      @property
      def email(self):
          return self._email
      
      @email.setter
      def email(self,email):
          self._email=email
          
          
    #Método str()  
    def __str__(self) -> str:
        return f"Persona: [ID: {self._id_persona} , Nombre: {self._nombre} , Apellido: {self._apellido} , Edad: {self._edad} , Email: {self._email}]"  
    
if __name__ == "__main__":    
 persona01=Persona(1,"Nicolás","Díaz",19,"nicolasdiazgarrido@gmail.com")
 log.debug(persona01)

 # Simular un insert
 persona01=Persona(nombre="Juan",apellido="Perez",email="pereznico@gmail.com") 
 log.debug(persona01)

# Simular un delete
persona01=Persona(id_persona=1)
log.debug(persona01)



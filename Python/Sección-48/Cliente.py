
from Logger_base import log

# Clase de cliente donde haremos todos sus metodos

class Cliente:
    
    
    @classmethod
    
    
    def __init__(self,id_cliente ,nombre, apellido,membresia):
      self._id_cliente=id_cliente
      self._nombre = nombre
      self._apellido = apellido
      self._membresia = membresia
      
    
    @property
    def id_cliente(self):
        return self._id_cliente  
    
    @id_cliente.setter
    def nombre(self,id_cliente):
        self._id_cliente=id_cliente
    
    @property
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
    def membresia(self):
        return self._membresia
           
    @membresia.setter
    def membresia(self,membresia):
        self._membresia=membresia
    
   
    def __str__(self) -> str:
        return f"Cliente [ID: {self._id_cliente} Nombre: {self._nombre} , Apellido: {self._apellido} , Membresia: {self._membresia}]"
    
                
if __name__ == "__main__":
    usuario02 = Cliente(1,"Nicolas","Diaz","2303")
    log.debug(usuario02)
            
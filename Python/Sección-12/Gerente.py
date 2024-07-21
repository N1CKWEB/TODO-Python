
from Empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre,sueldo,departamento):
      super().__init__(nombre,sueldo)  
      self._departamento = departamento
    
    
    #GET y SET
    @property
    def departamento(self):
        return self._departamento
    
    @departamento.setter
    def departamento(self,departamento):
        self._departamento=departamento   

    #Método str()
    def __str__(self) -> str:
        return f"Gerente: [Departamento: {self._departamento}] {super().__str__()}"

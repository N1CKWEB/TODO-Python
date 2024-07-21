# Polimorfismo en python

# Qué es?, significa multiples formas en tiempo de ejecución, es ejecutar multiples métodos en tiempo de ejecución, en sintesis el poliformismo es multiples formas en tiempo de ejecución



class Empleado:
    def __init__(self, nombre, sueldo):
      self._nombre = nombre
      self._sueldo = sueldo
      
    # GET y SET  
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre
        
    @property
    def sueldo(self):
        return self._sueldo
    
    @sueldo.setter
    def sueldo(self,sueldo):
        self._sueldo=sueldo
    
    
    #Método str()
    
    def __str__(self) -> str:
        return f"Empleado: [Nombre: {self._nombre} , Sueldo: {self._sueldo}]" 
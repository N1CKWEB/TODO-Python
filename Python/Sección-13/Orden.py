
from Computadora import Computadora


class Orden(Computadora):
    
    contadorOrdenes=0
    
    @classmethod
    def contador_estatico_orden(cls):
        cls.contadorOrdenes+=1
        return cls.contadorOrdenes
    
    
    def __init__(self,nombre,monitor,teclado,raton ):
        super().__init__(nombre,monitor,teclado,raton)
        self.__idOrden = Orden.contador_estatico_orden()
      
      
    #GET y SET
    @property
    def idOrden(self):
        return self.__idOrden
    
    @idOrden.setter
    def idOrden(self,idOrden):
        self.__idOrden=idOrden 
    
    #Método agregar computadoras:
    def agregarComputadora(self):
      pass  
    
    
    #Método str()
    def __str__(self) -> str:
        return f"Orden: [ID: {self.__idOrden} {super().__str__} ]"
    
    
    
    
    










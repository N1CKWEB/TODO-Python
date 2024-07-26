from Monitor import Monitor
from Teclado import Teclado
from Raton import Raton


class Computadora(Monitor,Teclado,Raton):
    
    contadorComputadoras=0
    
    @classmethod
    def contador_estatico_computadora(cls):
        cls.contadorComputadoras+=1
        return cls.contadorComputadoras
    
    def __init__(self,nombre,monitor,teclado,raton):
        super().__init__(monitor,teclado,raton)
        self.__idComputadora=Computadora.contador_estatico_computadora()
        self.__nombre = nombre
        
        
    #GET y SET
    @property
    def idComputadora(self):
        return self.__idComputadora
    
    @idComputadora.setter
    def idComputadora(self,idComputadora):
        self.__idComputadora=idComputadora 
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre 
        
    #Método str()
    def __str__(self) -> str:
        return f"Computadora: [ID: {self.__idComputadora} Nombre: {self.__nombre} {super().__str__()} ]" 
    
    
computadora01=Computadora("Lenovo","27p","Razer","Noga")

print(computadora01) 
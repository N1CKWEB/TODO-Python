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
        self._idComputadora=Computadora.contador_estatico_computadora()
        self._nombre = nombre
        self._monitor=monitor
        self._teclado=teclado
        self._raton=raton
        
        
    #GET y SET
    @property
    def idComputadora(self):
        return self._idComputadora
    
    @idComputadora.setter
    def idComputadora(self,idComputadora):
        self._idComputadora=idComputadora 
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre 
    
    @property
    def monitor(self):
        return self._monitor
    
    @monitor.setter
    def monitor(self,monitor):
        self._monitor=monitor
        
    @property
    def teclado(self):
        return self._teclado
    
    @teclado.setter
    def teclado(self,teclado):
        self._teclado=teclado 
        
    @property
    def raton(self):
        return self._raton
    
    @raton.setter
    def raton(self,raton):
        self._raton=raton 
        
    #Método str()
    def __str__(self) -> str:
        return f'''
     Nombre: {self._nombre}  ID: {self._idComputadora} [ 
     Monitor: {self._monitor}
     Teclado: {self._teclado}
     Raton: {self._raton} 
     ]''' 
     
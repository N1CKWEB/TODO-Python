
from Computadora import Computadora
from Monitor import Monitor
from Teclado import Teclado
from Raton import Raton

class Orden(Computadora):
    
    contadorOrdenes=0
    
    @classmethod
    def contador_estatico_orden(cls):
        cls.contadorOrdenes+=1
        return cls.contadorOrdenes
    
    
    def __init__(self,computadoras ):
        self._idOrden = Orden.contador_estatico_orden()
        self._computadoras=list(computadoras)
        # self._monitor=monitor
        # self._teclado=teclado
        # self._raton=raton
       
      
      
    #GET y SET
    @property
    def idOrden(self):
        return self._idOrden
    
    @idOrden.setter
    def idOrden(self,idOrden):
        self._idOrden=idOrden
   
    @property
    def computadoras(self):
        return self._computadoras
    
    @computadoras.setter
    def computadora(self,computadoras):
        self._computadoras=computadoras      
    
    #Método agregar computadoras:
    def agregarComputadora(self,computadora):
     self._computadoras.append(computadora)
    
    
    #Método str()
    def __str__(self) -> str:
        computadoras_str=" "
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__() + "|"
        return f'''
        Orden: [ID: {self._idOrden}  
      Computadora: {computadoras_str}]'''
    
    
monitor01=Monitor("Redragon",27)
teclado01=Teclado("USB","Redragon Kumara 65%")
raton01=Raton("USB","Noga Gamer X-Generación")    
    
monitor02=Monitor("Samsung Gaming",32)
teclado02=Teclado("USB","Auriculares Asus")
raton02=Raton("USB","Logitech")    
    
monitor03=Monitor("Asus Gaming",26)
teclado03=Teclado("USB","Logitech Black")
raton03=Raton("USB","Mouse HP")    
    
monitor04=Monitor("Philip Versión Gamer ",24)
teclado04=Teclado("USB","Auriculares HyperX")
raton04=Raton("USB","Mouse Redragon Cobra")    
    
computadora01=Computadora("PC Gamer",monitor01,teclado01,raton01)
computadora02=Computadora("Lenovo IDEAPAD Gaming 3",monitor02,teclado02,raton02)
    
computadora03=Computadora("PC Gamer Asus",monitor03,teclado03,raton03)
computadora04=Computadora("Computadora Gama ALTA ",monitor04,teclado04,raton04)

computadoras01=[computadora01,computadora02]    
computadoras02=[computadora03,computadora04]
orden01=Orden(computadoras01)
print(orden01)
orden02=Orden(computadoras02)    
print(orden02)










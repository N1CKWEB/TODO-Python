


class Monitor:
    
    contadorMonitores=0
    
    @classmethod
    def contador_estatico_monitor(cls):
          cls.contadorMonitores+=1
          return cls.contadorMonitores
    
    def __init__(self, marca,tamaño):
      self._idMonitor = Monitor.contador_estatico_monitor()
      self._marca = marca
      self._tamaño=tamaño
      
    #GET y SET
    
    @property
    def idMonitor(self):
        return self._idMonitor
    
    @idMonitor.setter
    def idMonitor(self,idMonitor):
        self._idMonitor=idMonitor 
    
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self,marca):
        self._marca=marca 
    
    @property
    def tamaño(self):
        return self._tamaño
    
    @tamaño.setter
    def tamaño(self,tamaño):
        self._tamaño=tamaño

    #Método str()
    def __str__(self) -> str:
        return f"Monitor: [ID: {self._idMonitor} Marca:{self._marca} Tamano: {self._tamaño} ]"
    
    
    
                                                          
                                                          
                                                         
                                                        
                                                        
    
    
    
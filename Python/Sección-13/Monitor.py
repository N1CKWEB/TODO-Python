


class Monitor:
    
    contadorMonitores=0
    
    @classmethod
    def contador_estatico_monitor(cls):
          cls.contadorMonitores+=1
          return cls.contadorMonitores
    
    def __init__(self, marca,tamaño):
      self.__idMonitor = Monitor.contador_estatico_monitor()
      self.__marca = marca
      self.__tamaño=tamaño
      
    #GET y SET
    
    @property
    def idMonitor(self):
        return self.__idMonitor
    
    @idMonitor.setter
    def idMonitor(self,idMonitor):
        self.__idMonitor=idMonitor 
    
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self,marca):
        self.__marca=marca 
    
    @property
    def tamaño(self):
        return self.__tamaño
    
    @tamaño.setter
    def tamaño(self,tamaño):
        self.__tamaño=tamaño

    #Método str()
    def __str__(self) -> str:
        return f"Monitor: [ID: {self.__idMonitor} Marca:{self.__marca} Tamano: {self.__tamaño} ]"
    
    
    
monitor01=Monitor("Samsung","24")

print(monitor01)
                                                         
                                                          
                                                          
                                                         
                                                        
                                                        
    
    
    
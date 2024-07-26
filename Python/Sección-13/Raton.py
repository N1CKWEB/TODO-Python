from DispositivoEntrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    
    contadorRatones=0
    
    @classmethod
    def contador_estatico_ratones(cls):
        cls.contadorRatones+=1
        return cls.contadorRatones
        
    def __init__(self,tipoEntrada, marca):
      super().__init__(tipoEntrada,marca)
      self.__idRaton = Raton.contador_estatico_ratones()
      
    #GET y SET
    
    @property
    def idRaton(self):
        return self.__idRaton
    
    @idRaton.setter
    def idRaton(self,idRaton):
        self.__idRaton=idRaton 
    
    
    
    #Método str()
    def __str__(self) -> str:
        return f"Raton: [ID: {self.__idRaton} {super().__str__()} ]"
    
    
    
    
raton01=Raton("USB","Lenovo")

print(raton01)
    
    
    
    

















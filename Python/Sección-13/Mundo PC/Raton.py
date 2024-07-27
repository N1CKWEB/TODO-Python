from DispositivoEntrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    
    contadorRatones=0
    
    @classmethod
    def contador_estatico_ratones(cls):
        cls.contadorRatones+=1
        return cls.contadorRatones
        
    def __init__(self,tipoEntrada, marca):
      self._idRaton = Raton.contador_estatico_ratones()
      super().__init__(tipoEntrada,marca)
      
    #GET y SET
    
    @property
    def idRaton(self):
        return self._idRaton
    
    @idRaton.setter
    def idRaton(self,idRaton):
        self._idRaton=idRaton 
    
    
    
    #Método str()
    def __str__(self) -> str:
        return f"Raton: [ID: {self._idRaton} Marca: {self._marca} Tipo de Entrada: {self._tipoEntrada} ]"
    
    
    
    
    
    

















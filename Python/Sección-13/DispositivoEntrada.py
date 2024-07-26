


class DispositivoEntrada:
    def __init__(self,tipoEntrada, marca):
      self.__tipoEntrada = tipoEntrada
      self.__marca = marca
      
    #GET y SET
    
    @property
    def tipoEntrada(self):
        return self.__tipoEntrada
    
    @tipoEntrada.setter
    def tipoEntrada(self,tipoEntrada):
        self.__tipoEntrada=tipoEntrada 
    
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self,marca):
        self.__marca=marca 
    
    
    #Método str()
    def __str__(self) -> str:
        return f"[TipoEntrada: {self.__tipoEntrada} Marca:{self.__marca} ]"
    
    
    
    
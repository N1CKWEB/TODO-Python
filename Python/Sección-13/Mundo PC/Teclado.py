from DispositivoEntrada import DispositivoEntrada



class Teclado(DispositivoEntrada):
    
    contadorTeclados=0
    
    @classmethod
    def contador_estatico_teclados(cls):
     cls.contadorTeclados+=1
     return cls.contadorTeclados
 
    def __init__(self,tipoEntrada,marca):
      self._idTeclado = Teclado.contador_estatico_teclados()
      super().__init__(tipoEntrada,marca)
   
   
    #GET y SET
    
    @property
    def idTeclado (self):
        return self._idTeclado   
   
    @idTeclado.setter
    def idTeclado(self,idTeclado):
        self._idTeclado=idTeclado

   
    #Método str()
    def __str__(self) -> str:
        return f"Teclado: [ID: {self._idTeclado} Marca: {self._marca} Tipo de Entrada: {self._tipoEntrada} ]"

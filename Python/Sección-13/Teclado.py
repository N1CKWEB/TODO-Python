from DispositivoEntrada import DispositivoEntrada



class Teclado(DispositivoEntrada):
    
    contadorTeclados=0
    
    @classmethod
    def contador_estatico_teclados(cls):
     cls.contadorTeclados+=1
     return cls.contadorTeclados
 
    def __init__(self,tipoEntrada,marca):
      super().__init__(tipoEntrada,marca)
      self.__idTeclado = Teclado.contador_estatico_teclados()
   
   
    #GET y SET
    
    @property
    def idTeclado (self):
        return self.__idTeclado   
   
    @idTeclado.setter
    def idTeclado(self,idTeclado):
        self.__idTeclado=idTeclado

   
    #Método str()
    def __str__(self) -> str:
        return f"Teclado: [ID: {self.__idTeclado} {super().__str__()} ]"


teclado01=Teclado("USB","HP")
teclado02=Teclado("Blueetoth","Lenovo")

print(teclado01)
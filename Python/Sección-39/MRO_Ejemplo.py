

# Ejercicio de Herencia



class Clase1:
    
    def __init__(self) -> None:
        print('Clase1.__init__')
   
   
   
    def metodo(self):
        print('Metodo clase 1')
    
     
class Clase2(Clase1):
    
    def __init__(self) -> None:
        print('Clase2.__init__')
        super().__init__()   
      
    def metodo(self):
        print('Metodo clase 2')
        super().metodo()
        
     
class Clase3(Clase1):
    
    def __init__(self) -> None:
        print('Clase3.__init__')
        super().__init__()   
        

      
    def metodo(self):
        print('Metodo clase 3') 
        super().metodo()
    
     
class Clase4(Clase2,Clase3):
   
     def metodo(self):
         print('Metodo clase 4')
         super().metodo()


class Clase5:
    pass     


clase04 = Clase4()

# base
print(Clase4.__base__)

# mro
print(Clase4.__mro__)


# Cúal metodo se ejecuta

clase04.metodo()












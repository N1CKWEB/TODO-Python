

# Ejercicio de Herencia



class Clase1:
    
    def __init__(self) -> None:
        print('Clase1.__init__')
   
   
   
    def metodo(self):
        print('Metodo clase 1')
    
     
class Clase2(Clase1):
    
    def __init__(self) -> None:
        super().__init__()
        print('Clase2.__init__')
           
      
    def metodo(self):
        super().metodo()
        print('Metodo clase 2')
    
     
class Clase3(Clase1):
    
    def __init__(self) -> None:
        super().__init__()
        print('Clase3.__init__')
        

      
    def metodo(self):
        super().metodo()
        print('Metodo clase 3') 
    
     
class Clase4(Clase2,Clase3):
   
     def metodo(self):
         super().metodo()       
         print('Metodo clase 4')
    
    
    
class Clase5:
    pass     


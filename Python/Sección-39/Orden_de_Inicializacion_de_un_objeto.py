


# Orden de inicialización de objetos

class Padre:
    def __init__(self) -> None:
        print('Inicializador Padre')

    
    
    def metodo(self):
        print('Metodo padre')


class Hija(Padre):
    # Se manda a llamar el método init de la clase padre, siempre cuando la clase hija no defina su propio metodo init
    
   def __init__(self) -> None:
       print('Inicializador hija')
       super().__init__()
   
   #Sobreescribimos el método heredado de la clase padre
   
   def metodo(self):
       print('Metodo sobreescrito hija') 
       super().metodo() 





hijo1=Hija()
hijo1.metodo()











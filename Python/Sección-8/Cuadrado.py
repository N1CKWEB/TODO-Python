from FiguraGeometrica import FiguraGeometrica 
from Color import Color
 

class Cuadrado(FiguraGeometrica,Color):
    def __init__ (self,lado,color):
        # super().__init__()
        FiguraGeometrica.__init__(self,lado,lado)
        Color.__init__(self,color)
     
    def calcular_area(self):
        return self.alto * self.ancho          
    
    #Método str() 
    def __str__(self) -> str:
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'
   
    
    
    
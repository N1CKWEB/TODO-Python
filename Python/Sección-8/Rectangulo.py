# Importamos las clases

from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Rectangulo(FiguraGeometrica,Color):
    def __init__ (self,ancho,alto,color):
        FiguraGeometrica.__init__(self,ancho,alto)
        Color.__init__(self,color)
        
    def calcular_area(self):
        return self.alto * self.ancho           
 
    #Método str() 
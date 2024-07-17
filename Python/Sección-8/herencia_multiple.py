# Herencia Multiple en python:

class FiguraGeometrica:
    def __init__ (self,alto,ancho):
        self._alto=alto
        self._ancho=ancho
        
    def __str__(self) -> str:
        return f"Figura Geometrica: [Alto: {self.alto}, Ancho:{self.ancho}]"
    
    #GET y SET
    @property
    def alto(self):
        return self._alto 
    
    @alto.setter
    def alto (self,alto):
        self._alto=alto
        
    @property
    def ancho(self):
        return self._ancho    
    
    @ancho.setter
    def ancho (self,ancho):
        self.ancho=ancho
        
class Color:
    def __init__ (self,color):
        self._color=color
        
    def __str__(self) -> str:
        return f"Color: [Color: {self.color} ]"
    
    #GET y SET
    @property
    def color(self):
        return self._color 
    
    @color.setter
    def color (self,color):
        self._color=color
        
class Cuadrado(FiguraGeometrica,Color):
    def __init__ (self,alto,ancho,color):
        super().__init__(alto,ancho,color)
        
    def __str__(self) -> str:
        return f"Color: [Color: {self.color} ]"
    
    #GET y SET
    @property
    def color(self):
        return self._color 
    
    @color.setter
    def color (self,color):
        self._color=color
        
        
               
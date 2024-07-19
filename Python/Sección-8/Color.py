class Color:
    def __init__ (self,color):
        self._color=color    
    
    #GET y SET
    @property
    def color(self):
        return self._color 
    
    @color.setter
    def color (self,color):
        self._color=color
        
    # Método str() 
    def __str__(self) -> str:
        return f"Color: [Color: {self._color} ]"
        
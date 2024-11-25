# Importamos las librerias

from PySide6.QtWidgets import QMainWindow,QLabel

# Componentes en pySide


class Componentes(QMainWindow):
    
    def __init__(self, name, age):
      super().__init__()
      self.setWindowTitle('Componentes') 
      
      #Creamos un componentes de tipo etiqueta (label) etiqueta
      etiqueta=QLabel('Hola')
      # Publicamos este componente
      self.setCentralWidget(etiqueta)
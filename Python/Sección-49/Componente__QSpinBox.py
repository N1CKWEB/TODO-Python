

# Importamos las clases

from PySide6.QtWidgets import QApplication,QWidget,QComboBox,QMainWindow,QListWidget,QLineEdit,QSpinBox
from PySide6.QtCore import Qt

class ComboBox(QMainWindow):
    
    
    def __init__(self,):
      super().__init__()
      self.setWindowTitle('ComboBox')
      # Componente QListWidget se parece al comboBox
      lista=QListWidget()
      # Agregamos elementos
      lista.addItems(['Uno','Dos','Tres'])
      
    # QSpinBox basicamente es para seleccionar un valor númerico
      numero=QSpinBox()
    
    # Rango de valores
      numero.setRange(-5,8)
      
    # Valores minimo
      numero.setMinimum(-5)
    # Valores maximo  
      numero.setMaximum(8)
    #  Establecemos prefijo y sufijo
      numero.setPrefix('$') 
      numero.setSuffix('c')
    # Establecemos el  salto (step)  
      numero.setSingleStep(3)
       
    # Nos conectamso al evento o señal de cambio de valor
    # Envia el valor numerico
      numero.valueChanged.connect(self.cambio_valor)
      numero.textChanged.connect(self.cambio_texto)  
      # Publicamos nuestro componente
      self.setCentralWidget(numero)
    def cambio_valor(self,nuevo_valor_numerico):
        print(f'Nuevo valor numerico: {nuevo_valor_numerico}')  
    
    def cambio_texto(self,nuevo_texto):
        print(f'Nuevo texto: {nuevo_texto}')
       
       
       
if __name__ == "__main__":
    app=QApplication([])
    ventana=ComboBox()
    ventana.show()
    app.exec() 
      
      
# Importamos las librerias
from PySide6.QtWidgets import QApplication,QMainWindow,QLabel,QCheckBox
from PySide6.QtCore import Qt
# from PySide6.QtGui import QPixmap
# Componentes en pySide


class Componentes(QMainWindow):
    
    
    def __init__(self):
      super().__init__()
      self.setWindowTitle('Componentes') 
      
      # Creamos un nuevo componente de checkbox
      checkbox=QCheckBox('Este es un checkbox')
      # Activamos el tercer estado
      # Tenemos tres estado 0-Apagar / 1-Sin Estado o parcialmente checado / 2-Encendido
      checkbox.setTristate(True)
      # Conectamos la señal de cambio de componente
      checkbox.stateChanged.connect(self.mostrar_estado)
      
      # Publicamos el componente 
      self.setCentralWidget(checkbox)
      
    
    def mostrar_estado(self, estado):
        print('Estado checkbox:', estado)
        # Trabajamos con las constantes
        if estado == Qt.Checked:
            print('Checkbox encendido')
        elif estado == Qt.PartiallyChecked:
            print('Checkbox sin estado o parcialmente checado')
        elif estado == Qt.Unchecked:
            print('Checkbox apagado')
        else:
            print('Checkbox con estado invalido')  
      
      
if __name__ == "__main__":
    app=QApplication([])
    ventana=Componentes()
    ventana.show()
    app.exec()

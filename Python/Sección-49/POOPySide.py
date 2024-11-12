# Importaciones
import sys
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow,QPushButton


class VentanaPySide(QMainWindow):
    
    def __init__(self):
      # Llamamos al metoodo _init_ de la clase padre
      super().__init__()
      self.setWindowTitle("POO con PySide")
      # self.resize(300,500)
      # colocamos los valores de ancho y alto de manera fija
      self.setFixedSize(QSize(300,500))
      
      # creamos el metodo de agregar componentes
      self._agregarComponentes()
      
    def _agregarComponentes(self):
        #  agregar un menu
        menu=self.menuBar()
        menu_archivo=menu.addMenu("Archivo")
        # Agregamos algunas opciones
        accion_nuevo=QAction('Nuevo',self)
        menu_archivo.addAction(accion_nuevo)
        # Agregamos un texto a la barra de estado
        accion_nuevo.setStatusTip("Crea un nuevo archivo")
        # Agregamos un nuevo mensaje en la barra de estado
        self.statusBar().showMessage('Información de la barra de estado...')
        
        # Agregamos un componente de un boton
        
        boton=QPushButton('Nuevo botón')
        # Publicamos el boton en la ventana
        self.setCentralWidget(boton)
        
      
      
      
      
      
      
      
if __name__ == "__main__":
    app=QApplication([])
    ventana=VentanaPySide()
    # Mostramo la ventana
    ventana.show()
    # Y con esto ejecutamos la aplicación
    sys.exit(app.exec())











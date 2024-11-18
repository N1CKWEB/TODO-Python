# Señales y Slots en PySide
import sys
from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton



class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals y Slots')
        # Boton
        self.boton=QPushButton('Click aqui')
        # Asociamos la señal de click al slot evento_click
        self.boton.clicked.connect(self.evento_click)
        # Conectar a la señal de cambio de titulo
        self.windowTitleChanged.connect(self.cambio_titulo_aplicacion)
        
        
        # # Conectamos el evento checado (por default el estado de nuestro componentes es False)
        # boton.setCheckable(True)
        # # Conectamos otro slot al evento checkable
        # boton.clicked.connect(self.evento_checar)
        # # Conectamos el evento (signal) click con el slot (evento_click)
        # boton.clicked.connect(self.evento_click)
        # publicamos el boton
        self.setCentralWidget(self.boton)
        
        
    # def evento_checar(self,checar):
    #     self.boton_checado=checar
    #     print('checado? ',self.boton_checado)
        
        
    # def evento_click(self):
    #     print('Has hecho click')    
    #     # Accedemos al estado del boton (checado)
    #     print('Boton checado desde evento click? ',self.boton_checado)
    
    def evento_click(self):
        # Cambiar el texto del boton y el título de la ventana
        self.boton.setText('Nuevo texto boton')
        self.boton.setEnabled(False)
        self.setWindowTitle('Nuevo titulo de la aplicacion') 
        print('evento_click')
        
    def cambio_titulo_aplicacion(self,nuevo_titulo):
        print(f'Nuevo titulo: {nuevo_titulo}')
        
            
        
        
if __name__ == "__main__":
    # Creamos el objeto de aplicación
    app=QApplication([]) 
    # Creamos una instancia de nuestra clase
    ventana=VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
    




























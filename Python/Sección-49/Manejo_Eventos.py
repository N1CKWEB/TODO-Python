# Señales y Slots en PySide
import sys
from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton,QLabel,QLineEdit,QVBoxLayout,QWidget



class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals y Slots')
        self.setFixedSize(400,200)
        # Definimos la etiqueta y línea de edición
        self.etiqueta=QLabel()
        self.entrada_texto=QLineEdit()
        # Conectar el Widget con entrada de texto
        # La señal es textChanged, y el slot es setText
        self.entrada_texto.textChanged.connect(self.etiqueta.setText)
        # Publicamos los componentes usando un layout
        disposicion=QVBoxLayout() 
        disposicion.addWidget(self.entrada_texto)
        disposicion.addWidget(self.etiqueta)
        # Crear un contenedor
        contenedor=QWidget()
        contenedor.setLayout(disposicion)
        # Publicamos el contenedor, el cual ya incluye los demas elementos
        self.setCentralWidget(contenedor)
        
        # Etiquetas en PySide
        

if __name__ == "__main__":
    # Creamos el objeto de aplicación
    app=QApplication([]) 
    # Creamos una instancia de nuestra clase
    ventana=VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
    




























# Importaciones
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys

# Hola Mundo en PySide

# Clase base de Qt (Pyside) 
# Se encarga de procesar los eventos de la aplicación

app=QApplication()
# Crear un objeto de ventana
# Cualquier componente puede ser una ventana
# ventana=QPushButton('Botón')
# ventana=QWidget()

ventana=QMainWindow() #Nos permite crear ventanas con diferentes componentes, y se encarga de gestionar la gestión de estas ventanas

# Mostrar la ventana
ventana.show()

# Cambiar el titulo de la ventana
ventana.setWindowTitle("Hola Mundo en PySide")

# Cambiar el tamaño de la ventana
ventana.resize(300,500)




# Se ejecuta la aplicación
sys.exit(app.exec())




































































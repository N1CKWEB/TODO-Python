

# Importamos las clases

from PySide6.QtWidgets import QApplication,QWidget,QComboBox,QMainWindow,QListWidget,QLineEdit
from PySide6.QtCore import Qt

class ComboBox(QMainWindow):
    
    
    def __init__(self,):
      super().__init__()
      self.setWindowTitle('ComboBox')
      # Componente QListWidget se parece al comboBox
      lista=QListWidget()
      # Agregamos elementos
      lista.addItems(['Uno','Dos','Tres'])
      
    # Componente nuevo para captar texto
      linea_texto=QLineEdit()  
    
    # Establecemos el maximo de caracteres a capturar
      linea_texto.setMaxLength(15) 
    # Establecemos un texto de ayuda 
      linea_texto.setPlaceholderText('Introducce tu nombre:')
    
    # Monitoreamos el evento change 
    
    # Caja de texto de solo lectrua
      # linea_texto.setReadOnly(True)
    
    # Monitorear enter, cmabio seleccionado texto, cambio texto
      linea_texto.returnPressed.connect(self.enter_presionado) 
      linea_texto.selectionChanged.connect(self.cambio_de_seleccion)
      linea_texto.textChanged.connect(self.nuevos_cambios)
      
   # Monitoreamos el cambio del elemento seleccionado, el elemento con el texto
      # lista.currentItemChanged.connect(self.cambio_elemento)
      # lista.currentTextChanged.connect(self.cambio_de_texto_nuevo)
      
      
      
      
      # self.setFixedSize(500,600)
    # Creamos un nuevo combo box (drop down list)
      # comboBox=QComboBox()
      
    # Monitoreamos el cambio de elemento seleccionado, tanto de indice como de texto
    #   comboBox.currentIndexChanged.connect(self.cambio_indice) 
    #   comboBox.currentTextChanged.connect(self.cambio_texto)
   
    # # Hacemos editable el comboBox 
    #   comboBox.setEditable(True)
    
    # Especificamos la 1pra politica de inserción
      # comboBox.setInsertPolicy(QComboBox.NoInsert)
    
    # Especificamos la 2da politica agregar al inicio de nuestro comboBox
      # comboBox.setInsertPolicy(QComboBox.InsertAtTop)
    
    # Modifica el elemento actual
      # comboBox.setInsertPolicy(QComboBox.InsertAtCurrent) 
     
    # Insertar al final de nuestro comboBox
      # comboBox.setInsertPolicy(QComboBox.InsertAtBottom)
      
    # Insertar después del elemento actual
      # comboBox.setInsertPolicy(QComboBox.InsertAfterCurrent)

      
    # Insertar alfabeticamente 
    #   comboBox.setInsertPolicy(QComboBox.InsertAlphabetically)
       
       
    # # Insertar antes del elemento actual
    #   # comboBox.setInsertPolicy(QComboBox.InsertBeforeCurrent)
       
    # # Limitar cuantos elementos agregamos al comboBox
    #   comboBox.setMaxCount(6)
   
       
       
    # # Agregamos elementos 
    #   comboBox.addItem('uno')
    #   comboBox.addItems(['dos','tres'])
      
      
      # Publicamos nuestro componente
      self.setCentralWidget(linea_texto)
  
    def cambio_elemento(self,nuevo_elemento):
      print(f"Nuevo elemento seleccionado: {nuevo_elemento.text()}")
      
    def cambio_indice(self,nuevo_indice):
      print(f'Nuevo indice seleccionado: {nuevo_indice}')    
    
    def cambio_de_texto_nuevo(self,nuevo_texto):
      print(f"Nuevo texto seleccionado 2: {nuevo_texto}")
      
    def cambio_texto(self,nuevo_texto):
      print(f"Nuevo texto seleccionado: {nuevo_texto}")
    
    def enter_presionado(self):
      print(f"Se presiono el __enter__")
      self.centralWidget().setText('Nicolas Ariel')
    
    def cambio_de_seleccion(self):
      print("Cambio seleccion texto")  
      print(self.centralWidget().selectedText())
    
    def nuevos_cambios(self,nuevos_cambios):
       print("Cambio de texto")   
       print(nuevos_cambios)
       
       
       
       
if __name__ == "__main__":
    app=QApplication([])
    ventana=ComboBox()
    ventana.show()
    app.exec() 
      
      
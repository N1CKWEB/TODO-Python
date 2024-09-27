
# Importamos las librerias

import tkinter as tk


class EditorDeTexto(tk.Tk):

     def __init__(self,):
       super().__init__()
       
       self.title('Editor De Texto')
       #Configuración tamaño mínimo de la venta
       self.rowconfigure(0,minsize=600,weight=1)
       #Configuración mínima de la segunda columna
       self.columnconfigure(1,minsize=600,weight=1)
      # Atributo de campo de texto
       self.campo_texto=tk.Text(self,wrap=tk.WORD)     
      # Atributo de archivo 
       self.archivo=None 
      # Atributo para saber si ya se abrió un archivo anteriormente
       self.archivo_abierto=False
      
      


if __name__ == "__main__":
    
    editor=EditorDeTexto()
    editor.mainloop()
    










import tkinter as tk
from tkinter import messagebox

class Calculadora(tk.Tk):
    
     def __init__(self):
       super().__init__()
       self.title('Calculadora')
       self.geometry('400x500')
       self.iconbitmap('C:/Users/LENOVO/OneDrive/Documentos/Ruta de Python Developer/Python/Sección-44/calculadora.ico')
       self.resizable(0,0)
       # Atributo de clase
       self.expresion = ''
      #  Caja de texto (input)
       self.entrada=None
      # StringVar la utilizamos para obtener el valor del input
       self.entrada_texto=tk.StringVar()
      # Creamos los componentes
       self._creacion_componentes()
              
       
      #  Método de Clase
      # Método para crear los componentes
     def _creacion_componentes(self):
      
      # Creamos un frame para la caja de texto
      entrada_frame=tk.Frame(self,width=400,height=50,background='grey')  
      entrada_frame.pack(side=tk.TOP)
      
      # Caja de texto
      entrada=tk.Entry(entrada_frame,font=('arial',18,'bold'), 
                       textvariable=self.entrada_texto,width=30,justify=tk.RIGHT)
      entrada.grid(row=0,column=0,ipady=10)
      
      # Creamos otro frame para la parte inferior
      botones_frame=tk.Frame(self,width=400,height=450, background='blue')
      botones_frame.pack()
      
      
      # Primer renglón
      boton_limpiar=tk.Button(botones_frame,text='C',command=self.evento_limpiar,width='32',height=3,border=0,background='green',cursor='hand2')
      
      boton_limpiar.grid(row=0,column=0,columnspan=3,padx=1,pady=1)
      boton_limpiar.pack() 
      
     def evento_limpiar(self):
         pass  
       
       
       
       
       
if __name__ == "__main__":
    calculadora=Calculadora()
    calculadora.mainloop()







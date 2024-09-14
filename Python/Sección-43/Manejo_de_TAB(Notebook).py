
import tkinter as tk
from tkinter import ttk,messagebox

# Manejo de Tabuladores (Notebook) en Tkinter


ventana=tk.Tk()

ventana.title('Componentes')
ventana.geometry('600x400')

ventana.iconbitmap('C:/Users/LENOVO/OneDrive/Documentos/Ruta de Python Developer/Python/Sección-43/icono.ico')




def crear_tabs():
  # Creamos un tab central, para ello usamos la clase de Notebook 
  control_tabulador=ttk.Notebook()
  #  Un (frame) nos va a permitir agregar más componentes  dentro de cada uno de nuestro tabuladores 
  tabulador_1=ttk.Frame(control_tabulador)
  tabulador_2=ttk.Frame(control_tabulador)
  # Agregamos el tabulador al control de  tabuladores
  control_tabulador.add(tabulador_1,text='Tabulador 1')
  control_tabulador.add(tabulador_2,text='Tabulador 2')
  # Mostramos el tabulador
  control_tabulador.pack(fill='both') 
  
  # Agregamos una etiqueta y un componente de entrada
  etiqueta1=ttk.Label(tabulador_1,text='Nombre: ')
  etiqueta1.grid(row=0,column=0,sticky=tk.E)
  entrada1=ttk.Entry(tabulador_1,width=30) 
  entrada1.grid(row=0,column=1,padx=5,pady=5)  
  
  def enviar():
      messagebox.showinfo('Mensaje ', f"Nombre: {entrada1.get()}")
  
  # Agregamos un botón
  boto1=ttk.Button(tabulador_1,text='Enviar',command=enviar)
  boto1.grid(row=1,column=0,columnspan=2)
     
 
crear_tabs() 
ventana.mainloop()







# Clase de AppZonaFit donde agregaremos todos los metodos 
import tkinter as tk
from tkinter import ttk,messagebox



class App(tk.Tk):
       
       COLOR_VENTANA="#1d2d44"
       
       def __init__(self):
           super().__init__()
           self.configurar_ventana()
           self.configurar_grid()
           self.mostrar_titulo()
           self.mostrar_formulario()
        # #  Mostrar la tabla
           self.mostrar_tablas()
           
       def configurar_ventana(self):
               
            self.title('Zona Fit App')          
            self.geometry('700x500')
            self.configure(background=App.COLOR_VENTANA)
            
            self.resizable(0,0)
          # Creamos un estilo
            self.estilos = ttk.Style()
            self.estilos.theme_use('clam')
            self.estilos.configure(self, background=App.COLOR_VENTANA, foreground='white',
                         fieldbackground='black')
            self.estilos.configure('TButton', background='#005f73')
            self.estilos.map('TButton', background=[('active', '#0a9396')])
   
            
       def configurar_grid(self):     
          
          self.columnconfigure(0,weight=1)
          self.columnconfigure(1,weight=1)
          
           
       def mostrar_titulo(self):
          
          # Título  
          etiqueta=ttk.Label(self,text='Zona Fit (GYM)',font=('Arial',20),background=App.COLOR_VENTANA,foreground='white')
          
          etiqueta.grid(row=0,column=0,columnspan=2,pady=30)
          
       def mostrar_formulario(self):
          
          # Nombre  
          nombre_caja_de_texto=ttk.Entry(self)
          nombre_caja_de_texto.grid(row=1,column=1,sticky=tk.E,padx=5,pady=5)   
     
          # Apellido
          apellido_etiqueta=ttk.Label(self,text='Apellido')
          apellido_etiqueta.grid(row=2,column=0,sticky=tk.W,padx=5,pady=5)
          
          apellido_caja_de_texto=ttk.Entry(self)
          apellido_caja_de_texto.grid(row=2,column=1,sticky=tk.E,padx=5,pady=5)   
     

          # Membresia
          membresia_etiqueta=ttk.Label(self,text='Membresia')
          membresia_etiqueta.grid(row=3,column=0,sticky=tk.W,padx=5,pady=5)

          membresia_caja_de_texto=ttk.Entry(self)
          membresia_caja_de_texto.grid(row=3,column=1,sticky=tk.E,padx=21,pady=19)   
          
          
          # Boton guardar

          # boton_guardar=ttk.Button(self,text='Guardar')
          # boton_guardar.grid(row=5,column=0,sticky=tk.BOTTOM)
          
          # # Boton eliminar

          # boton_eliminar=ttk.Button(self,text='Eliminar')
          # boton_eliminar.grid(row=5,column=1,sticky=tk.BOTTOM)
          
          # # Boton limpiar

          # boton_limpiar=ttk.Button(self,text='Limpiar')
          # boton_limpiar.grid(row=5,column=2,sticky=tk.BOTTOM)
  
          # Asociar eventos al boton de login
          # boton_guardar.bind('<Return>',validar) 
          # boton_eliminar.bind('<Return>',validar) 
          # boton_limpiar.bind('<Return>',validar) 
          
          # boton_guardar.bind('<Button-1>',validar) 
          # boton_eliminar.bind('<Button-1>',validar) 
          # boton_limpiar.bind('<Button-1>',validar) 
       def mostrar_tablas(self):     
          # Creamos un frame para mostar la tabla
          self.frame_table=ttk.Frame(self)
          # Definimos los estilos de la tabla
          
              
if __name__ == "__main__":
    appFit=App()
    appFit.mainloop()
             



















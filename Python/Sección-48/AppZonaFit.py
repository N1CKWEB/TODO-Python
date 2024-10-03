

# Clase de AppZonaFit donde agregaremos todos los metodos 
import tkinter as tk
from tkinter import ttk,messagebox



class App(tk.Tk):
       
       
       
       def __init__(self):
           super().__init__()
           self.configurar_ventana()
           self.configurar_grid()
           
        # #  Mostrar la tabla
        #    self.mostrar_tablas()
           
       def configurar_ventana(self):
               
            self.title('Zona Fit App')          
            self.geometry('600x400')
            self.configure(background='#1d2d44')
            self.resizable(0,0)
            
       def configurar_grid(self):     
            self.columnconfigure(0,weight=1)
            self.columnconfigure(1,weight=0)
            
       def mostrar_tabla(self):     
           pass



if __name__ == "__main__":
    appFit=App()
    appFit.mainloop()
             



















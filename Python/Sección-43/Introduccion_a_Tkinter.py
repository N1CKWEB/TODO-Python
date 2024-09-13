

# Introducción  a Tkinter


# GUI - Graphical User Interface

# Tkinter - TK Interface

# Importamos el modulo de tkinter
import tkinter as tk
# Importamos el módulo del tema de tkinter
from tkinter import ttk

# Creamos un objeto usando la clase TK
ventana=tk.Tk()

# Modificamos el tamaño de nuestra ventana (pixeles)
ventana.geometry('600x400')

# Cambiamos el nombre de la ventana
ventana.title('Primera ventana con Tkinter!!!')


# Configuramos el icono de la aplicación

ventana.iconbitmap('C:/Users/LENOVO/OneDrive/Documentos/Ruta de Python Developer/Python/Sección-43/icono.ico')


def evento_click_2():
    boton2.config(text='Boton presionado 2')
    print('Ejecucion del evento click 2')
    
    # Creamos un nuevo componente y los mostramos
    boton3=ttk.Button(ventana,text='Nuevo boton 2')
    boton3.pack() 

# Creamos un método
def evento_click():
    # Modifica el texto del boton
    boton1.config(text='Boton presionado')
    print('Ejecucion del evento click')
    # Creamos un nuevo componente y los mostramos
    boton2=ttk.Button(ventana,text='Nuevo boton')
    boton2.pack()
    

# Creamos un boton (widget), el objeto padre es la ventana
boton1=ttk.Button(ventana,text='Dar Click',command=evento_click)
boton2=ttk.Button(ventana,text='Dar Click segunda vez',command=evento_click_2)

# Utilizar el pack layout manager para mostrar el botón de la ventana
boton1.pack()
boton2.pack()

# Inicializamos la ventana (esta línea la ejecutamos al final)
# Si la ejecutamos antes, no se van a mostrar los cambios anteriores
ventana.mainloop() #Con este metodo mostramos la ventana, si o si tenes que usar este método para visualizar la ventana 










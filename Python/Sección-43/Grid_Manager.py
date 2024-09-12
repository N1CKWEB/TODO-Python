import tkinter as tk

# Importamos el módulo del tema de tkinter
from tkinter import ttk



ventana=tk.Tk()

ventana.geometry('600x400')

ventana.title('Manejo de Grid')

ventana.iconbitmap('C:/Users/LENOVO/OneDrive/Documentos/Ruta de Python Developer/Python/Sección-43/icono.ico')

# Configuramos el grid

ventana.rowconfigure(0,weight=2)
ventana.rowconfigure(1,weight=10)
ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=5)


# Definimos metodos

def evento_uno():
   boton1.config(text='Boton 1 presionado',fg='black',relief=tk.GROOVE,background='red')
    
# def evento_dos():
#     boton2.config(text='Boton 2 presionado',fg='black',relief=tk.GROOVE,background='green')
    

# def evento_tres():
#    boton3.config(text='Boton 3 presionado',fg='black',relief=tk.GROOVE,background='purple') #relief cambia el entorno del boton    
    
# def evento_cuatro():
    # boton4.config(text='Boton 4 presionado', fg='black',relief=tk.GROOVE,
                #   background='blue')
    
    
# Definimos dos botones

# N(arriba),E(derecha),S(abajo),W(izquierda)
boton1=tk.Button(ventana,text='Boton 1',command=evento_uno)
# boton2=tk.Button(ventana,text='Boton 2 ',command=evento_dos)
# boton3=tk.Button(ventana,text='Boton 3',command=evento_tres)
# boton4=tk.Button(ventana,text='Boton 4',command=evento_cuatro)


# Manejo de grid, digamos para colocar la posiciones de los botones donde queramos en la pantalla

# sticky=pegajoso (se queda ifjo en uno solo lugar)
# i = inner que seria un espacio que dejamos de manera interna para el pady o el ipady para el padding en tkinter
boton1.grid(row=0,column=0,sticky='NSWE',padx=40, pady=30,ipadx=20,ipady=50,columnspan=2,rowspan=2)
# boton2.grid(row=1,column=0,sticky='NSWE')
# boton3.grid(row=0,column=1,sticky='NSWE')
# boton4.grid(row=1,column=1,sticky='NSWE')


ventana.mainloop()






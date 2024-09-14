
import tkinter as tk
from tkinter import ttk,messagebox

# Manejo de variables y componenetes Entry

ventana=tk.Tk()

ventana.geometry('600x400')

ventana.title('Manejo de Variables y Componentes Entry')

ventana.iconbitmap('C:/Users/LENOVO/OneDrive/Documentos/Ruta de Python Developer/Python/Sección-43/icono.ico')



# Definimos una variable que podremos modificar posteriormente (set), leer(get)
# entrada_var1=tk.StringVar(value='Valor por default')
entrada=tk.Entry(ventana,width=30)
entrada.grid(row=0,column=0)


# Etiqueta (label)
etiqueta=tk.Label(ventana,text='Aqui se mostrara el contenido de la caja de texto')
etiqueta.grid(row=1,column=0,columnspan=2)


def enviar():
    # Recuperamos la información a partir de la variable asociada a la caja de texto
    # boton1.config(text=entrada.get())
   # Si queremos realizar una modificación utilizamos la variable de texto y el método set()
    # entrada_var1.set('Cambio....')
    # Recuperamos la información 
    # print(entrada.get())
    # Modificamos el texto del label
    etiqueta.config(text=entrada.get())
    # Messagebox (caja de mensaje)
    mensaje1=entrada.get()
    if mensaje1:
     messagebox.showinfo('Mensaje informativo',mensaje1 + ' informativo')
     messagebox.showerror('Mensaje de error',mensaje1 + ' error')
     messagebox.showwarning('Mensaje de alerta',mensaje1+ ' alerta')
    
# Lo primero que se coloca en el boton es el componente padre que sería la ("ventana"), 
boton1=tk.Button(ventana,text='Enviar',command=enviar)
boton1.grid(row=0,column=1,sticky='NSWE')




ventana.mainloop()









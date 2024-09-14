

import tkinter as tk

from tkinter import ttk

# Componente entry en Tkinter 

# La caja de texto para interactuar con la GUI es entry

ventana=tk.Tk()

ventana.geometry('600x400')

ventana.title('Componente Entry')

ventana.iconbitmap('C:/Users/LENOVO/OneDrive/Documentos/Ruta de Python Developer/Python/Sección-43/icono.ico')

# width es la cantidad de caracteres que ocupa la caja


# justify es para alinear el texto a donde quieras vos, y podemos utilizar la propiedad de show para mostrar ese caracteres como queramos, y la propiedad DISABLED es para desabilitar un campo, y NORMAL para habilitar la caja de texto
# entrada1=ttk.Entry(ventana,width=30,justify=tk.CENTER,show='*')  
entrada1=ttk.Entry(ventana,width=30,justify=tk.CENTER,state=tk.NORMAL)  
entrada1.grid(row=0,column=0)

# insert agrega un texto a nuestra caja de texto
entrada1.insert(0,'Introduce tu nombre')
# tk.END significa que podemos agregar a nuestra caja existente al final algo
entrada1.insert(tk.END,'.')
# Esto es para hacer que solo sea lectura la caja de texto,se agrega después que se pone el componente y su mensaje 
# entrada1.config(state='readonly')

def enviar():
    
    if entrada1.get() == 'Nicolas':
        boton1.config(text='correcto')
        print('Nombre correcto')   
        # Eliminar contenido
        # entrada1.delete(0,tk.END)
        # Seleccionar el texto de la caja
        entrada1.select_range(0,tk.END)
        # Para hacer efectiva la seleccion del texto
        entrada1.focus() 
            
    else:
        boton1.config(text='incorrecto')
        print('Nombre incorrecto')


# Lo primero que se coloca en el boton es el componente padre que sería la ("ventana"), 
boton1=tk.Button(ventana,text='Enviar',command=enviar)
boton1.grid(row=1,column=1)



ventana.mainloop()




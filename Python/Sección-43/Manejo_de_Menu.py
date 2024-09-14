
# Manejo de Menu en Tkinter Python
import sys
import tkinter as tk
from tkinter import ttk,messagebox,Menu

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
    etiqueta.config(text=entrada.get())
    mensaje1=entrada.get()
    if mensaje1:
        messagebox.showinfo('Mensaje informativo',mensaje1 + ' informativo')

def salir():
    # quit() hace que se quita la ventana
    ventana.quit()    
    # destroy hace que se destruya la ventana
    ventana.destroy()
    # sys.exit() lo que hace es que sale del progreso
    print('Salimos..')
    sys.exit()
    
    
def crear_menu():
    # Configuramos el menu principal
    menu_principal=Menu(ventana)
    # tearoff = False para evitar que se separe el menu de la interfaz
    sub_menu_archivo=Menu(menu_principal,tearoff=False)
    # Agregamos una nueva opción al menu de archivo
    sub_menu_archivo.add_command(label='Nuevo')
    # Agregamos un separador
    sub_menu_archivo.add_separator() 
    # Agregamos la opción de salir
    # Agregamos el submenu al menu principal
    sub_menu_archivo.add_command(label='Salir',command=salir)
    menu_principal.add_cascade(menu=sub_menu_archivo,label='Archivo')
    # Submenu de ayuda
    sub_menu_ayuda=Menu(menu_principal,tearoff=False)
    sub_menu_ayuda.add_command(label='Acerca De')
    menu_principal.add_cascade(menu=sub_menu_ayuda,label='Ayuda')
    
    # Mostramos el menu en la ventana principal
    ventana.config(menu=menu_principal)
    
    
    
    
    
        
# Lo primero que se coloca en el boton es el componente padre que sería la ("ventana"), 
boton1=tk.Button(ventana,text='Enviar',command=enviar)
boton1.grid(row=0,column=1,sticky='NSWE')

crear_menu()


ventana.mainloop()












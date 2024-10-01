
import tkinter as tk
from tkinter import ttk,messagebox,scrolledtext


# Manejo de tablas en python
ventana=tk.Tk()
ventana.title('Manejo de Tabla')
ventana.geometry('600x400')
ventana.configure(background='#1d2d44')
ventana.resizable(0,0)



# Configurar el grid

ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=0)
# Definir un estilo

estilo=ttk.Style()
estilo.theme_use('clam') #preparar el manejo del tema oscuro
estilo.configure('Treeview',
                 background='black',
                 foreground='white',
                 fieldbackground='black',
                 rowheight=30) 
estilo.map('Treeview',background=[('selected','#3a86ff')])


# Definir las columnas
columnas=('Id','Nombre','Edad')
tabla=ttk.Treeview(ventana,columns=columnas,show='headings')



# Cabecera de la tabla
tabla.heading('Id',text='Id',anchor=tk.CENTER)
tabla.heading('Nombre',text='Nombre',anchor=tk.W)
tabla.heading('Edad',text='Edad',anchor=tk.W)

# Formato a las columnas 
tabla.column('Id',width=80)
tabla.column('Nombre',width=120)
tabla.column('Edad',width=120)


# Cargar datos a la tabla
# datos=( (1,'Nicolas',19),
#         (2,'Juan',19),
#         (3,"Naim",19),
#         (4,"Nacho",19) )


datos= ((1,"Nicolas",19),(2,"Juan",19),(3,"Naim",19),(4,"Nacho",19)) + ((1,"Nicolas",19),(2,"Juan",19),(3,"Naim",19),(4,"Nacho",19)) + ((1,"Nicolas",19),(2,"Juan",19),(3,"Naim",19),(4,"Nacho",19)) + ((1,"Nicolas",19),(2,"Juan",19),(3,"Naim",19),(4,"Nacho",19)) + ((1,"Nicolas",19),(2,"Juan",19),(3,"Naim",19),(4,"Nacho",19)) + ((1,"Nicolas",19),(2,"Juan",19),(3,"Naim",19),(4,"Nacho",19))


for persona in datos:
    tabla.insert(parent='',index=tk.END,values=persona) 

# Scroll de la tabla
scroll=ttk.Scrollbar(ventana,orient=tk.VERTICAL,command=tabla.yview)
tabla.configure(yscroll=scroll.set)
scroll.grid(row=0,column=1,sticky=tk.NS)

#Publicar nuestra tabla
tabla.grid(row=0,column=0,sticky=tk.NSEW) 


ventana.mainloop()

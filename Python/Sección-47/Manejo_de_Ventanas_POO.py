


# Manejo de ventanas con POO


import tkinter as tk
from tkinter import ttk,messagebox


class App(tk.Tk):
    
    def __init__(self ):
      super().__init__() #Constructor de la clase padte Tk
      self.configurar_ventana()
      self.configurar_grid()
    #   Mostrar la tabla
      self.mostrar_tabla()
      
    def configurar_ventana(self):
         self.geometry('600x400')     
         self.configure(background='#1d2d44')
         self.title('Manejo de ventanas con POO')
         self.resizable(0,0)
         
    def configurar_grid(self):
         self.columnconfigure(0,weight=1)
         self.columnconfigure(1,weight=0)

    def mostrar_tabla(self):               
        # Agregando los estilos  
        estilo=ttk.Style()
        estilo.theme_use('clam') #preparar el manejo del tema oscuro
        estilo.configure('Treeview',
                        background='black',
                        foreground='white',
                        fieldbackground='black',
                        rowheight=30) 
        estilo.map('Treeview',background=[('selected','#3a86ff')])
        columnas=('Id','Nombre','Edad')
        self.tabla=ttk.Treeview(self,columns=columnas,show='headings')    
                  
        # Cabecera de la tabla
        self.tabla.heading('Id',text='Id',anchor=tk.CENTER)
        self.tabla.heading('Nombre',text='Nombre',anchor=tk.W)
        self.tabla.heading('Edad',text='Edad',anchor=tk.W)

        # Formato a las columnas 
        self.tabla.column('Id',width=80)
        self.tabla.column('Nombre',width=120)
        self.tabla.column('Edad',width=120)
                
        # Cargar datos a la tabla
        datos=( (1,'Nicolas',19),
                (2,'Juan',19),
                (3,"Naim",19),
                (4,"Nacho",19) )
        for persona in datos:
            self.tabla.insert(parent='',index=tk.END,values=persona)   
        
        #  Scroll de la tabla
        scroll=ttk.Scrollbar(self,orient=tk.VERTICAL,command=self.tabla.yview)
        self.tabla.configure(yscroll=scroll.set)
        scroll.grid(row=0,column=1,sticky=tk.NS) 
        
        # asociar el evento select de la tabla
        self.tabla.bind('<<TreeviewSelect>>',self.mostrar_registro_seleccionado)
        
        #Publicar nuestra tabla
        self.tabla.grid(row=0,column=0,sticky=tk.NSEW) 

        
        # Definimos el método mostrar registro seleccionado
    def mostrar_registro_seleccionado(self,event):
        print('Ejecutando metodo mostrar registro seleccionado')
        elemento_seleccionado=self.tabla.selection()[0] #Solo procesamos el primer registro 
        elemento=self.tabla.item(elemento_seleccionado) #item
        persona=elemento['values'] #tupla de una persona
        print(persona)  
        messagebox.showinfo('Persona seleccionado',message=f'Persona: {persona}')




if __name__ == "__main__":
    appPOO=App()
    appPOO.mainloop()
             
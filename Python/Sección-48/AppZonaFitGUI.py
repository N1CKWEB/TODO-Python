

# Clase de AppZonaFitGUI donde haremos la GUI (Interfaz Grafica) 

import tkinter as tk
from tkinter import ttk, messagebox
from ClienteDAO import ClienteDAO_NEW
from Cliente import Cliente

class App(tk.Tk):
    COLOR_VENTANA = "#1d2d44"
    
    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.cargar_tabla()
        self.mostrar_scrollbar()
        self.mostrar_botones()

    def configurar_ventana(self):
        self.title('Zona Fit App')
        self.geometry('700x500')
        self.configure(background=App.COLOR_VENTANA)
        self.resizable(0, 0)

        self.estilos = ttk.Style()
        self.estilos.theme_use('clam')
        self.estilos.configure('TLabel', background=App.COLOR_VENTANA, foreground='white')
        self.estilos.configure('TButton', background='#005f73')
        self.estilos.map('TButton', background=[('active', '#0a9396')])

    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def mostrar_titulo(self):
        etiqueta = ttk.Label(self, text='Zona Fit (GYM)', font=('Arial', 20))
        etiqueta.grid(row=0, column=0, columnspan=2, pady=30)

    def mostrar_formulario(self):
        # Crear estilo para los frames
        self.estilos.configure('TFrame', background=App.COLOR_VENTANA)

        # Crear el frame del formulario y aplicar el estilo
        self.frame_form = ttk.Frame(self, style='TFrame')

        # Nombre
        nombre_etiqueta = ttk.Label(self.frame_form, text='Nombre')
        nombre_etiqueta.grid(row=0, column=0, sticky=tk.W, padx=30, pady=5)
        self.nombre_caja_de_texto = ttk.Entry(self.frame_form)
        self.nombre_caja_de_texto.grid(row=0, column=1, sticky=tk.E, padx=5, pady=5)

        # Apellido
        apellido_etiqueta = ttk.Label(self.frame_form, text='Apellido')
        apellido_etiqueta.grid(row=1, column=0, sticky=tk.W, padx=30, pady=5)
        self.apellido_caja_de_texto = ttk.Entry(self.frame_form)
        self.apellido_caja_de_texto.grid(row=1, column=1, sticky=tk.E, padx=5, pady=5)

        # Membresía
        membresia_etiqueta = ttk.Label(self.frame_form, text='Membresía')
        membresia_etiqueta.grid(row=2, column=0, sticky=tk.W, padx=30, pady=5)
        self.membresia_caja_de_texto = ttk.Entry(self.frame_form)
        self.membresia_caja_de_texto.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)
        
        # Publicar el frame de forma
        self.frame_form.grid(row=1, column=0)

    def cargar_tabla(self):
        self.frame_table = ttk.Frame(self)
        self.frame_table.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

        self.estilos.configure('Treeview', background='black', foreground='white', fieldbackground='black', rowheight=20)

        columnas = ('Id', 'Nombre', 'Apellido', 'Membresía')
        self.tabla = ttk.Treeview(self.frame_table, columns=columnas, show='headings')

        for col in columnas:
            self.tabla.heading(col, text=col)
        self.tabla.grid(row=0, column=0)

        self.tabla.column('Id', anchor=tk.CENTER, width=50)
        self.tabla.column('Nombre', anchor=tk.W, width=100)
        self.tabla.column('Apellido', anchor=tk.W, width=100)
        self.tabla.column('Membresía', anchor=tk.W, width=100)

        self.cargar_datos()

    def cargar_datos(self):
        self.tabla.delete(*self.tabla.get_children())  # Limpiar tabla antes de cargar datos
        clientes = ClienteDAO_NEW.seleccionar_bd()
        for cliente in clientes:
            self.tabla.insert(parent='', index=tk.END, values=(cliente.id_cliente, cliente.nombre, cliente.apellido, cliente.membresia))

    def mostrar_scrollbar(self):
        scroll = ttk.Scrollbar(self.frame_table, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scroll.set)
        scroll.grid(row=0, column=1, sticky=tk.NS)

    def validar_cliente(self):
        # Validamos los campos
        if self.nombre_caja_de_texto.get() and self.apellido_caja_de_texto.get() and self.membresia_caja_de_texto.get():
            if self.validar_membresia():
                self.guardar_cliente()
            else:
                messagebox.showerror('Atención', "El valor de membresía no es numérico")
                self.membresia_caja_de_texto.delete(0, tk.END)
                self.membresia_caja_de_texto.focus_set()
        else:
            messagebox.showerror('Atención', 'Debe llenar el formulario')
            self.nombre_caja_de_texto.focus_set()

    def validar_membresia(self):
        try:
            int(self.membresia_caja_de_texto.get())
            return True
        except ValueError:
            return False

    def guardar_cliente(self):
        nombre = self.nombre_caja_de_texto.get()
        apellido = self.apellido_caja_de_texto.get()
        membresia = self.membresia_caja_de_texto.get()
        cliente = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
        ClienteDAO_NEW.insertar_bd(cliente)
        messagebox.showinfo('Agregar', 'Cliente agregado')
        # Volvemos a mostrar los datos y limpiamos el formulario
        self.recargar_datos()

    def recargar_datos(self):
        # Volver a cargar los datos de la tabla
        self.cargar_datos()
        # Limpiar el formulario
        self.limpiar_formulario()

    def mostrar_botones(self):
        self.frame_botones = ttk.Frame(self, style='TFrame')

        # Botón guardar
        boton_guardar = ttk.Button(self.frame_botones, text='Guardar', command=self.validar_cliente)
        boton_guardar.grid(row=0, column=0, padx=30)

        # Botón eliminar
        boton_eliminar = ttk.Button(self.frame_botones, text='Eliminar', command=self.eliminar_cliente)
        boton_eliminar.grid(row=0, column=1, padx=30)

        # Botón limpiar
        boton_limpiar = ttk.Button(self.frame_botones, text='Limpiar', command=self.limpiar_cliente)
        boton_limpiar.grid(row=0, column=2, padx=30)

        self.frame_botones.grid(row=2, column=0, columnspan=2, pady=20)

    def eliminar_cliente(self):
        selected_item = self.tabla.selection()
        if selected_item:
            cliente_id = self.tabla.item(selected_item)['values'][0]
            ClienteDAO_NEW.eliminar_bd(cliente_id)
            self.recargar_datos()
            messagebox.showinfo('Eliminar', 'Cliente eliminado')
        else:
            messagebox.showerror('Error', 'Debe seleccionar un cliente')

    def limpiar_cliente(self):
        self.limpiar_formulario()

    def limpiar_formulario(self):
        self.nombre_caja_de_texto.delete(0, tk.END)
        self.apellido_caja_de_texto.delete(0, tk.END)
        self.membresia_caja_de_texto.delete(0, tk.END)

if __name__ == "__main__":
    appFit = App()
    appFit.mainloop()

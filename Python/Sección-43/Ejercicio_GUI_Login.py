# Ejercicio Propuesto: GUI de Login con Tkinter

import tkinter as tk
from tkinter import ttk, messagebox

class Login(tk.Tk):
    
    def __init__(self):
        super().__init__()
        # Ventana principal
        self.title('Login')
        self.geometry('300x130')
        self.iconbitmap('C:/Users/LENOVO/OneDrive/Documentos/Ruta de Python Developer/Python/Sección-43/icono.ico')
        self.resizable(0, 0)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self._crear_componentes()
        
    # Definir el método crear componentes
    def _crear_componentes(self):
        # Usuario y Password
        self.entrada_1 = tk.Entry(self, width=34, justify=tk.CENTER)
        self.entrada_2 = tk.Entry(self, width=34, show='*', justify=tk.CENTER)
        
        self.entrada_1.grid(row=0, column=2, padx=5, pady=5)
        self.entrada_2.grid(row=1, column=2, padx=5, pady=5)
        
        etiqueta_1 = tk.Label(self, text='Usuario:', fg='blue')
        etiqueta_2 = tk.Label(self, text='Password:', fg='blue')

        etiqueta_1.grid(row=0, column=0, sticky='NSWE', padx=6, pady=5)
        etiqueta_2.grid(row=1, column=0, sticky='NSWE', padx=6, pady=5)
        
        # Botón login
        boton_login = tk.Button(self, text='Login', command=self._enviar, fg='blue', background='black')
        boton_login.grid(row=2, column=2, sticky=tk.W, padx=5, pady=5)
        
    # Definir el método enviar fuera del crear_componentes
    def _enviar(self):
        usuario = self.entrada_1.get()
        password = self.entrada_2.get()
        
        if usuario and password:
            messagebox.showinfo('Datos Login', f'Usuario:  {usuario}     Password:  {password}')
            self.entrada_1.delete(0, tk.END)
            self.entrada_2.delete(0, tk.END)
        else:
            messagebox.showwarning('Advertencia', 'Por favor, complete ambos campos.')

if __name__ == '__main__':
    login_ventana = Login()
    login_ventana.mainloop()

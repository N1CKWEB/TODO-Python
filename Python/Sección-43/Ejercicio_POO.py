import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from time import sleep

# Manejo de Tabuladores (Notebook) en Tkinter
class Componentes(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Componentes')
        self.geometry('600x400')
        self.iconbitmap('C:/Users/LENOVO/OneDrive/Documentos/Ruta de Python Developer/Python/Sección-43/icono.ico')
        self.crear_tabs()

    def _crear_componentes_del_tabulador(self, tabulador):
        # Cambiado: Ahora los componentes se agregan al tabulador, no al root (self)
        etiqueta1 = ttk.Label(tabulador, text='Nombre: ')
        etiqueta1.grid(row=0, column=0, sticky=tk.E)
        entrada1 = ttk.Entry(tabulador, width=30)
        entrada1.grid(row=0, column=1, padx=5, pady=5)

        def enviar():
            messagebox.showinfo('Mensaje', f"Nombre: {entrada1.get()}")

        boto1 = ttk.Button(tabulador, text='Enviar', command=enviar)
        boto1.grid(row=1, column=0, columnspan=2)

    def _crear_componente_tabulador3(self, tabulador):
        contenido = 'Este es mi texto con el contenido'
        scroll = scrolledtext.ScrolledText(tabulador, width=50, height=10, wrap=tk.WORD)
        scroll.insert(tk.INSERT, contenido)
        scroll.grid(row=0, column=0)

    def _crear_componente_tabulador4(self, tabulador):
        datos = [x + 1 for x in range(10)]
        comboBox = ttk.Combobox(tabulador, width=15, values=datos)
        comboBox.grid(row=0, column=0, padx=10, pady=10)
        comboBox.current(1)

        def mostrar_valor():
            messagebox.showinfo('Valor seleccionado', f"Valor seleccionado: {comboBox.get()}")

        boton2 = ttk.Button(tabulador, text='Mostrar valor seleccionado', command=mostrar_valor)
        boton2.grid(row=0, column=1)

    def _crear_componente_tabulador5(self, tabulador):
        imagen = tk.PhotoImage(file='C:/Users/LENOVO/OneDrive/Documentos/Ruta de Python Developer/Python/Sección-43/python-logo.png')
         
        def mostrar_detalles_imagen():
            messagebox.showinfo('Mas info de la imagen', f"Nombre de la imagen: {imagen.cget('file')}")

        boton_imagen = ttk.Button(tabulador, image=imagen, command=mostrar_detalles_imagen)
        boton_imagen.grid(row=0, column=0)

        imagen_2 = tk.PhotoImage(file='C:/Users/LENOVO/OneDrive/Documentos/Ruta de Python Developer/Python/Sección-43/Trainsmart.png')
         
        def mostrar_detalles_imagen_2():
            messagebox.showinfo('Mas info de la imagen', f"Nombre de la imagen: {imagen_2.cget('file')}")

        boton_imagen_2 = ttk.Button(tabulador, image=imagen_2, command=mostrar_detalles_imagen_2)
        boton_imagen_2.grid(row=1, column=0,padx=4,pady=10)

    def _crear_componente_tabulador6(self, tabulador):
        barra_progreso = ttk.Progressbar(tabulador, orient='horizontal', length=550)
        barra_progreso.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

        def ejecutar_barra():
            barra_progreso['maximum'] = 100
            for valor in range(101):
                sleep(0.05)
                barra_progreso['value'] = valor
                barra_progreso.update()
            barra_progreso['value'] = 0

        def ejecutar_ciclo():
            barra_progreso.start()

        def detener():
            barra_progreso.stop()

        def detener_despues():
            esperar_ms = 1000
            self.after(esperar_ms, barra_progreso.stop)

        boton_inicio = ttk.Button(tabulador, text='Ejecutar barra de progreso', command=ejecutar_barra)
        boton_inicio.grid(row=1, column=0)
        boton_ciclo = ttk.Button(tabulador, text='Ejecutar ciclo', command=ejecutar_ciclo)
        boton_ciclo.grid(row=1, column=1)
        boton_detener = ttk.Button(tabulador, text='Detener ejecucion', command=detener)
        boton_detener.grid(row=1, column=2)
        boton_despues = ttk.Button(tabulador, text='Detener ejecucion despues', command=detener_despues)
        boton_despues.grid(row=1, column=3)

    def crear_tabs(self):
        control_tabulador = ttk.Notebook(self)
        tabulador_1 = ttk.Frame(control_tabulador)
        tabulador_2 = ttk.Frame(control_tabulador)

        control_tabulador.add(tabulador_1, text='Tabulador 1')
        control_tabulador.add(tabulador_2, text='Tabulador 2')
        control_tabulador.pack(fill='both', expand=True)  # Mantén `pack` aquí para el Notebook

        self._crear_componentes_del_tabulador(tabulador_1)
        
        tabulador_3 = ttk.LabelFrame(control_tabulador, text='Contenido')
        control_tabulador.add(tabulador_3, text='Tabulador 3')
        self._crear_componente_tabulador3(tabulador_3)

        tabulador_4 = ttk.LabelFrame(control_tabulador, text='Contenido')
        control_tabulador.add(tabulador_4, text='Tabulador 4')
        self._crear_componente_tabulador4(tabulador_4)

        tabulador_5 = ttk.LabelFrame(control_tabulador, text='Contenido')
        control_tabulador.add(tabulador_5, text='Tabulador 5')
        self._crear_componente_tabulador5(tabulador_5)

        tabulador_6 = ttk.LabelFrame(control_tabulador, text='Contenido')
        control_tabulador.add(tabulador_6, text='Tabulador 6')
        self._crear_componente_tabulador6(tabulador_6)

if __name__ == "__main__":
    componentes = Componentes()
    componentes.mainloop()

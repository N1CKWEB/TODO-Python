
import tkinter as tk
from tkinter import ttk,messagebox,scrolledtext
from time import sleep
# Manejo de Tabuladores (Notebook) en Tkinter


ventana=tk.Tk()

ventana.title('Componentes')
ventana.geometry('600x400')

ventana.iconbitmap('C:/Users/LENOVO/OneDrive/Documentos/Ruta de Python Developer/Python/Sección-43/icono.ico')


def crear_componentes_del_tabulador(tabulador):
   # Agregamos una etiqueta y un componente de entrada
  etiqueta1=ttk.Label(tabulador,text='Nombre: ')
  etiqueta1.grid(row=0,column=0,sticky=tk.E)
  entrada1=ttk.Entry(tabulador,width=30) 
  entrada1.grid(row=0,column=1,padx=5,pady=5)  
  
  def enviar():
      messagebox.showinfo('Mensaje ', f"Nombre: {entrada1.get()}")
  
  # Agregamos un botón
  boto1=ttk.Button(tabulador,text='Enviar',command=enviar)
  boto1.grid(row=1,column=0,columnspan=2)
 
def crear_componente_tabulador3(tabulador):
  
  contenido='Este es mi texto con en el contenido'
  # Creamos el componente scrool, y siempre ahí que poner el wrap con tk.WORD para completar la palabra
  scroll=scrolledtext.ScrolledText(tabulador,width=50,height=10,wrap=tk.WORD)
  scroll.insert(tk.INSERT,contenido)
  # Mostramos el componente
  scroll.grid(row=0,column=0)
   
def crear_componente_tabulador4(tabulador): 
   
  # Creamos una lista usando data list comprehensions
  datos=[x+1 for x in range(10)]  
  comboBox=ttk.Combobox(tabulador,width=15,values=datos)
  comboBox.grid(row=0,column=0,padx=10,pady=10)
  # Selecciona un elemento por default o mostrar
  comboBox.current(1)
   # Agregamos un boton para saber que opción seleccionó el usuario
  def mostrar_valor():
     messagebox.showinfo('Mostrar valor seleccionado',f"Valor seleccionado: {comboBox.get()}")  
     
  boton2=ttk.Button(tabulador,text='Mostrar valor seleccionado',command=mostrar_valor) 
  boton2.grid(row=0,column=1)
  
def crear_componente_tabulador5(tabulador):
  # Agregamos una imagen
  imagen=tk.PhotoImage(file='C:/Users/LENOVO/OneDrive/Documentos/Ruta de Python Developer/Python/Sección-43/python-logo.png')
  def mostrar_detalles_imagen():
       messagebox.showinfo('Mas info de la imagen', f"Nombre de la imagen: {imagen.cget("file")}")
  boton_imagen=ttk.Button(tabulador,image=imagen,command=mostrar_detalles_imagen)
  boton_imagen.grid(row=0,column=0)  
  
    
def  crear_componente_tabulador6(tabulador):
  # Creamos el componnete de barra de progreso
  barra_progreso=ttk.Progressbar(tabulador,orient='horizontal',length=550)
  barra_progreso.grid(row=0,column=0,padx=10,pady=10,columnspan=4)
  
  # Metodos para controlar los eventos de la barra de progreso
  def ejecutar_barra():
    barra_progreso['maximum']=100
    for valor in range(101):
        # Mandamos a esperar un poco antes de continuar con la ejecución de la barra
        sleep(0.05)
        # Incremenetamos nuestra barra de progreso
        barra_progreso['value']=valor
        # Actualizamos nuestra barra de progreso
        barra_progreso.update()
    
    barra_progreso['value']=0    
  
  def ejecutar_ciclo():
   barra_progreso.start()
  
  def detener():
    barra_progreso.stop()
    
  def detener_despues():
      esperar_ms=1000
      ventana.after(esperar_ms,barra_progreso.stop)
        
  # Botones para controlar los eventos de una barra de progreso
  boton_inicio=ttk.Button(tabulador,text='Ejecutar barra de progreso',command=ejecutar_barra)
  boton_inicio.grid(row=1,column=0)
  boton_ciclo=ttk.Button(tabulador,text='Ejecutar ciclo',command=ejecutar_ciclo)
  boton_ciclo.grid(row=1,column=1)
  boton_detener=ttk.Button(tabulador,text='Detener ejecucion',command=detener)
  boton_detener.grid(row=1,column=2)
  boton_despues=ttk.Button(tabulador,text='Detener ejecucion despues',command=detener_despues)
  boton_despues.grid(row=1,column=3)
  
  
def crear_tabs():
  # Creamos un tab central, para ello usamos la clase de Notebook 
  control_tabulador=ttk.Notebook()
  #  Un (frame) nos va a permitir agregar más componentes  dentro de cada uno de nuestro tabuladores 
  tabulador_1=ttk.Frame(control_tabulador)
  tabulador_2=ttk.Frame(control_tabulador)
  # Agregamos el tabulador al control de  tabuladores
  control_tabulador.add(tabulador_1,text='Tabulador 1')
  control_tabulador.add(tabulador_2,text='Tabulador 2')
  # Mostramos el tabulador
  control_tabulador.pack(fill='both') 
  
  # Creamos los componentes del  tabulador 1
  crear_componentes_del_tabulador(tabulador_1) 
  # Creamos un segundo tabulador 
  tabulador_3=ttk.LabelFrame(control_tabulador,text='Contenido')
  control_tabulador.add(tabulador_3,text='Tabulador 3')
  
  # Creamos los componentes del segundo tabulador 3
  crear_componente_tabulador3(tabulador_3)
    
  #Crear otro tabulador
  tabulador_4=ttk.Labelframe(control_tabulador,text='Contenido')
  control_tabulador.add(tabulador_4,text='Tabulador 4') 
    
  crear_componente_tabulador4(tabulador_4)  
 
   #Creamos otro tabulador
  tabulador_5=ttk.LabelFrame(control_tabulador,text='Contenido')
  control_tabulador.add(tabulador_5,text='Tabulador 5')
  
  crear_componente_tabulador5(tabulador_5)  
 
   #Creamos otro tabulador
  tabulador_6=ttk.LabelFrame(control_tabulador,text='Contenido')
  control_tabulador.add(tabulador_6,text='Tabulador 6')
  
  crear_componente_tabulador6(tabulador_6)  
 
  
crear_tabs() 
ventana.mainloop()





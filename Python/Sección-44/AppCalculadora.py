import tkinter as tk
from tkinter import messagebox

class Calculadora(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title('Calculadora')
        self.geometry('324x450')  # Tamaño de la ventana
        self.resizable(False, False)  # Evitar que la ventana se redimensione
        self.iconbitmap('C:/Users/LENOVO/OneDrive/Documentos/Ruta de Python Developer/Python/Sección-44/calculadora.ico')
        # Atributo de clase
        self.expresion = ''
        # Caja de texto (input)
        self.entrada = None
        # StringVar la utilizamos para obtener el valor del input
        self.entrada_texto = tk.StringVar()
        # Creamos los componentes
        self._creacion_componentes()
              
       
    # Método para crear los componentes
    def _creacion_componentes(self):
        # Creamos un frame para la caja de texto
        entrada_frame = tk.Frame(self, width=400, height=50, background='darkblue')  
        entrada_frame.pack(side=tk.TOP)
      
        # Caja de texto
        entrada = tk.Entry(entrada_frame, font=('arial',18,'bold'), 
                           textvariable=self.entrada_texto, width=24, justify=tk.RIGHT)
        entrada.grid(row=0, column=0, ipady=10)
      
        # Creamos otro frame para la parte inferior
        botones_frame = tk.Frame(self, width=400, height=550, background='white')
        botones_frame.pack()
      
        # Primer renglón
        # Botón de limpiar
        boton_limpiar = tk.Button(botones_frame, text='C', command=self.evento_limpiar, width='32', height=3, border=0, background='red', cursor='hand2')
        boton_limpiar.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
      
        # Botón dividir /  
        boton_dividir = tk.Button(
          botones_frame, text='/', command=lambda: self.evento_dividir('/'), width=10, height=3, border=0, background='red', cursor='hand2').grid(row=0, column=3, padx=1, pady=1)
        
      
        # Segundo renglón

        # Boton siete
        boton_siete=tk.Button(botones_frame,text='7',command=lambda: self.evento_siete(7),width=10,height=3,border=0,background='red',cursor='hand2').grid(row=1,column=0,padx=1,pady=1)

        # Boton ocho        
        boton_ocho=tk.Button(botones_frame,text='8',command=lambda: self.evento_ocho(8),width=10,height=3,border=0,background='red',cursor='hand2').grid(row=1,column=1,padx=1,pady=1)
        
        # Boton nueve
        boton_nueve=tk.Button(botones_frame,text='9',command=lambda: self.evento_nueve(9),width=10,height=3,border=0,background='red',cursor='hand2').grid(row=1,column=2,padx=1,pady=1)
        
        # Boton multiplicar *
        boton_multiplicar=tk.Button(botones_frame,text='*',command=lambda: self.evento_multiplicar('*'),width=10,height=3,border=0,background='red',cursor='hand2').grid(row=1,column=3,padx=1,pady=1)
        
        
        # Tercer renglón
        
        # Boton cuatro
        boton_cuatro=tk.Button(botones_frame,text='4',command=lambda: self.evento_cuatro(4),width=10,height=3,border=0,background='red',cursor='hand2').grid(row=2,column=0,padx=1,pady=1)
        
        # Boton cinco
        boton_cinco=tk.Button(botones_frame,text='5',command=lambda: self.evento_cinco(5),width=10,height=3,border=0,background='red',cursor='hand2').grid(row=2,column=1,padx=1,pady=1)
        
        # Boton seis
        boton_seis=tk.Button(botones_frame,text='6',command=lambda: self.evento_seis(6),width=10,height=3,border=0,background='red',cursor='hand2').grid(row=2,column=2,padx=1,pady=1)
        
        # Boton menos -
        boton_menos=tk.Button(botones_frame,text='-',command=lambda: self.evento_cuatro('-'),width=10,height=3,border=0,background='red',cursor='hand2').grid(row=2,column=3,padx=1,pady=1)
        
        # Cuarto renglón

        # Boton uno
        boton_uno=tk.Button(botones_frame,text='1',command=lambda: self.evento_uno(1),width=10,height=3,border=0,background='red',cursor='hand2').grid(row=3,column=0,padx=1,pady=1)
        
        # Boton dos
        boton_dos=tk.Button(botones_frame,text='2',command=lambda: self.evento_dos(2),width=10,height=3,border=0,background='red',cursor='hand2').grid(row=3,column=1,padx=1,pady=1)
        
        # Boton tres
        boton_tres=tk.Button(botones_frame,text='3',command=lambda: self.evento_tres(3),width=10,height=3,border=0,background='red',cursor='hand2').grid(row=3,column=2,padx=1,pady=1)
        
        # Boton más +
        boton_mas=tk.Button(botones_frame,text='+',command=lambda: self.evento_mas('+'),width=10,height=3,border=0,background='red',cursor='hand2').grid(row=3,column=3,padx=1,pady=1)
        
        
        # Quinto renglón
        
        # Boton cero
        boton_cero=tk.Button(botones_frame,text='0',command=lambda: self.evento_cero(0), width=21, height=3, border=0, background='red', cursor='hand2').grid(row=4,column=0,columnspan=2,padx=1,pady=1)
        
        
        # Boton punto .
        boton_punto=tk.Button(botones_frame,text='.',command=lambda: self.evento_punto('.'),width=10,height=3,border=0,background='red',cursor='hand2').grid(row=4,column=2,padx=1,pady=1)
        
        
        # Boton resultado =
        boton_resultado=tk.Button(botones_frame,text='=',command=lambda: self.evento_resultado('='),width=10,height=3,border=0,background='red',cursor='hand2').grid(row=4,column=3,padx=1,pady=1)
        
        
        
    def evento_limpiar(self):
        self.expresion = '' 
        self.entrada_texto.set(self.expresion)
         
    def evento_dividir(self, elemento):
        # Concatenamos el nuevo elemento a la expresión ya existente
        self.expresion = f'{self.expresion} {elemento}' 
        self.entrada_texto.set(self.expresion)  
       
    def evento_siete(self,elemento):
       self.expresion=f'{self.expresion} {elemento}'
       self.entrada_texto.set(self.expresion)   
       
    def evento_ocho(self,elemento):
       self.expresion=f'{self.expresion} {elemento}'
       self.entrada_texto.set(self.expresion)   
       
    def evento_nueve(self,elemento):
       self.expresion=f'{self.expresion} {elemento}'
       self.entrada_texto.set(self.expresion)   
       
    def evento_multiplicar(self,elemento):
       self.expresion= f'{self.expresion} {elemento}'
       self.entrada_texto.set(self.expresion)   
       
    def evento_cuatro(self,elemento):
       self.expresion= f'{self.expresion} {elemento}'
       self.entrada_texto.set(self.expresion)   
       
    def evento_cinco(self,elemento):
       self.expresion= f'{self.expresion} {elemento}'
       self.entrada_texto.set(self.expresion)   
       
    def evento_seis(self,elemento):
       self.expresion= f'{self.expresion} {elemento}'
       self.entrada_texto.set(self.expresion)   
       
    def evento_menos(self,elemento):
       self.expresion= f'{self.expresion} {elemento}'
       self.entrada_texto.set(self.expresion)   
       self.entrada_texto.set(self.expresion)   
       
    def evento_uno(self,elemento):
       self.expresion= f'{self.expresion} {elemento}'
       self.entrada_texto.set(self.expresion)   
       self.entrada_texto.set(self.expresion)   
       
    def evento_dos(self,elemento):
       self.expresion= f'{self.expresion} {elemento}'
       self.entrada_texto.set(self.expresion)   
       self.entrada_texto.set(self.expresion)   
       
    def evento_tres(self,elemento):
       self.expresion= f'{self.expresion} {elemento}'
       self.entrada_texto.set(self.expresion)   
       
       
    def evento_mas(self,elemento):
       self.expresion= f'{self.expresion} {elemento}'
       self.entrada_texto.set(self.expresion)   
       
       
    def evento_cero(self,elemento):
       self.expresion= f'{self.expresion} {elemento}'
       self.entrada_texto.set(self.expresion)   
       
       
    def evento_punto(self,elemento):
       self.expresion= f'{self.expresion} {elemento}'
       self.entrada_texto.set(self.expresion)   
       
       
    def evento_resultado(self,elemento):
       self.expresion= f'{self.expresion} {elemento}'
       self.entrada_texto.set(self.expresion)   
       
       
       
       
if __name__ == "__main__":
    calculadora = Calculadora()
    calculadora.mainloop()


import inspect
# Decoradores de Clases

# Permite tranformar de manera programática nuestra clase
# Es similar a los decoradores de funciones (es metaprogramación)

def decorador_repr(cls):
    print('1.Se ejecuta el decorador de nuestra clase')
    print(f"Recibimos el objeto de la clase: {cls.__name__}")
    
    # Revisamos los atributos de la clase con en el método vars
    atributos=vars(cls)
    # Iteramos cada uno de los atributos
    # for nombre,atributo in atributos.items():
    #      print(nombre,atributo)
    
    # Revisamos si se ha sobreescrito el método __init__
    if "__init__" not in atributos:
        raise TypeError (f"{cls.__name__} no ha sobreescrito el metodo __init__")  
    firmar_init=inspect.signature(cls.__init__)
    print(f"Firma del metodo __init__: {firmar_init}")
    # Recuperamos los parametros, excepto el primero que es self 
    parametros__init__=list(firmar_init.parameters)[1:]
    print(f"Parametros __init__: {parametros__init__}")

    # Revisamos si cada parametro tiene un método property  asociado
    for parametro in parametros__init__:
        #property es un valor de tipo built-in para preguntar si se esta utilizando el  decorador property
        es_metodo_property=isinstance(atributos.get(parametro),property)
        if not es_metodo_property:
            raise TypeError(f"No existe un metodo property para el parametro: {parametro}")
    
    #Creamos el método repr dinamicamente
    def metodo_repr(self):
        # Obtenemos el nombre de la clase dinámicamente
        nombre_clase=self.__class__.__name__
        print(f"Nombre clase: {nombre_clase}")
        # Obtenemos los nombres de las propiedades y sus valores  dinámicamente
        # Expresión generadora, crear nombre_atr=valor_atr
        generador_arg=(f"{nombre}={getattr(self,nombre)!r}" for nombre in parametros__init__)
        # Lista de argumentos
        lista_de_argumentos=list(generador_arg)
        print(f'Lista del generador: {lista_de_argumentos}')
        # Creamos la cadena a partir de la lista de argumentos
        argumentos=', '.join(lista_de_argumentos)
        print(f"Argumentos del metodo repr: {argumentos}")
        resultado_metodo_repr=f'{nombre_clase}({argumentos})'    
        print(f"El resultado del metodo repr: {resultado_metodo_repr}") 
        return resultado_metodo_repr
    
    #Agregar dinamicamente el método repr a nuestra clase
    setattr(cls,'__repr__',metodo_repr) #Agrega un método __repr__
      
         
    return cls


    

@decorador_repr
class Persona:
    
    def __init__(self,nombre,apellido) -> None:
        print('2.Se ejecuta el inicializador')
        self._nombre=nombre
        self._apellido=apellido
    
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre
   
    @apellido.setter
    def apellido(self,apellido):
        self._apellido=apellido
        
    # def __repr__(self) -> str:
    #     return f"{__class__.__name__} [Nombre: {self._nombre} , Apellido: {self._apellido} ]"
    
    

persona1=Persona("Nicolas","Diaz")    
persona2=Persona("Sergio","Diaz")    

print(f"La persona es: {persona1!r}")
print(f"La persona es: {persona2!r}")



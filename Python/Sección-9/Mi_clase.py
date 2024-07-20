# Resumen:
# Métodos de Instancia: Manipulan o acceden a los datos de una instancia específica.
# Métodos Estáticos: Ejecutan funciones relacionadas con la clase, sin acceso a la instancia.
# Métodos de Clase: Acceden y modifican el estado de la clase en lugar de las instancias.
# Decoradores: Modifican el comportamiento de otras funciones o métodos de manera clara y concisa.


from Constantes import MI_CONSTANTE
from Constantes import Matematicas as Mate


class MiClase:
    
    variable_clase="Valor variable clase"
    
    def __init__(self,variable_instancia):
        self.variable_instancia=variable_instancia
        
    # Método estáticos en python
    @staticmethod
    def metodo_estatico():
       print(MiClase.variable_clase) 
    
    # Método de clase en python, y "cls" es una referencia a la clase misma
    @classmethod
    def metodo_de_clase(cls):
        print(cls.variable_clase)    
        
    # Método de instancia
    def metodo_instancia(self):
        self.metodo_de_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)
 

print(MiClase.variable_clase)        

miClase01=MiClase("Valor variable instancia")

print(miClase01.variable_instancia)


miClase02=MiClase("Otro valor de variable instancia")


# Creación de variables de Clase al vuelo en python
MiClase.variable_clase2="Valor variable clase 2"

print(miClase02.variable_clase2)
print(miClase02.variable_instancia)

print(miClase02.variable_clase)

MiClase.metodo_estatico()
MiClase.metodo_de_clase()


miObjeto01 = MiClase("variable_instancia")

miObjeto01.metodo_de_clase()

print(miObjeto01.variable_instancia)

miObjeto01.metodo_instancia()


print(MI_CONSTANTE)

# No debemos cmabiar el valor de una constante
MI_CONSTANTE="Nuevo valor de mi constante"

print(MI_CONSTANTE)


print(Mate.PI)


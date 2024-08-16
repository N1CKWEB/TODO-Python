

# Alcances de variables - También conocido como (scape)

var_global='Variable global'


def imprimir():
   #Acceder a una variable global
   global var_global
   print(f'Variable global pero ascedida desde una funcion: {var_global}')   
   var_global='Nuevo valor de la variable global, fue modificada'
   #Definir variable local
   var_local='Variable local'    
   print(f'Variable local pero ascedida desde una funcion: {var_local}')   
   
   def funcion_anidada():
       print(f'Variable local dentro de la funcion anidada: {var_local}')
       
   funcion_anidada()   
       
imprimir()
print(var_global)



# Alcance de variables - Parte 2







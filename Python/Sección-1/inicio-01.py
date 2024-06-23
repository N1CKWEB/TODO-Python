
#Ejercicio-Saludar a la consola
print("""Este es mi saludos desde Python!""")


#VARIABLES EN PYTHON

mi_variable="Hola desde Python"
numeros=23

print(mi_variable) 
print(numeros)


x=10
y=2
z=x+y
print(z)

#Dirección de Memoria y Variables en Python

# "id()" se usa para ver la dirección de memoria que esta guardado la variable


print(id(x))

print(id(y))

print(id(z))


#Ejercicio-Declaración de Variables

mi_nombre="Nicolas"
mi_numero=21444552
mi_correo="nicolasdiaz23@gmail.com"

print(mi_nombre , " ", mi_numero , " " , mi_correo)

#Tipos de datos en Python

# Numeric:Interger, Complex Number, Float
# Dictionary
# Boolean
# Set
# Sequence Type: Strings, List, Tuple


num=10

palabra: int="Python" # En python se puede asignarle a una variable el tipo de dato, no es muy común usarlo, pero se puede

dicionario=("","")

print(type(dicionario))

#Tipo Int 
n1=23
print(type(n1))

#Tipo String
n2="N1ck"
print(type(n2))

#Tipo Float 
n3=23.3
print(type(n3))

#Tipo Boolean
n4=True
print(type(n4))


#Cadena (String)

mi_grupo_favorito="COLDPLAY"

print("Mi grupo favorito de musica es: " + mi_grupo_favorito)
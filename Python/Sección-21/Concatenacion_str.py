from Mi_clase import MiClase


# Profundizando en el tipo str

# Concatenación automatica 

mensaje="Hola" "Mundo"
mensaje +="Universidad" "Python"
print(mensaje)



# Solicitar ayuda (método help), nos ayuda para poder buscar cualquier tipo de dato en python, ya sea un modulo o libreria, método,clases o lo que sea



help(str.capitalize)


# Uso de docstring en python:

help(MiClase)

# El método __doc__  llama la documentación de la clase y la definición de la clase
print(MiClase.__doc__)
print(MiClase.__init__.__doc__)
print(MiClase.mi_metodo.__doc__)
print(MiClase.mi_metodo)
print(type(MiClase.mi_metodo))


# Inmutable = No Modificable
# help(str.capitalize),
mensaje1="hola mundo"
mensaje2=mensaje1.capitalize()
print(f"Mensaje 1: {mensaje1}, id: {hex(id(mensaje1)) }")
print(f"Mensaje 2: {mensaje2}, id:  {hex(id(mensaje2))}")
mensaje1+="adios"
print(f"Mensaje 1: {mensaje1}, id: {hex(id(mensaje1)) }")

# Método join para cadenas, un iterable que es lo que se le pasa a este metodo puede ser una lista, cadena,diccionario un objeto que podemos iterar varios objetos, join significa "unir"

# help(str.join)

tupla_str=("Hola","Mundo","Universidad","Python")

mensaje_new=' '.join(tupla_str)

print(f"Mensaje  {mensaje_new}")

lista_cursos=["Java","Python","DJango","Flask","SpringBoot"]

mensaje=', '.join(lista_cursos)

print(mensaje)



cadena="HolaMundo"
mensaje5=".".join(cadena)
print(mensaje5)


diccionario={
    "Nombre":"Nico",
    "Apellido":"Diaz",
    "Edad":"19"
}

llaves='-'.join(diccionario.keys())
valores='-'.join(diccionario.values())

print(f"Llaves: {llaves}, el tipo es: {type(llaves)}")
print(f"Valores: {valores}, el tipo es: {type(llaves)}")


# Método split para cadenas, es para separar o dividir

# help(str.split)


cursos='Java Python Javascript Angular Spring Excel'

listas_cursos=cursos.split()
print(listas_cursos)


cursos_separados_por_coma="Java,Python,Django,Flask,SQL,PostgreSQL"

lista_cursos_2=cursos_separados_por_coma.split(',')

print(lista_cursos_2)
print(len(lista_cursos_2))


lista_cursos_2=cursos_separados_por_coma.split(', ',3)

print(lista_cursos_2)

# Formato de str con Parámetros Posicionales
# Usamos parametros posicionales

nombre="Nico"
edad=19

mensaje_con_formato="Mi nombre es: %s y mi edad es %d"%(nombre,edad)

print(mensaje_con_formato)


# Tenemos dos formatos para mostrar los parametros
persona=("Carla","Riquelme",5000.00)

# Primer formato 1:
mensaje_con_formato_2="Hola mi nombre es %s y mi apellido es %s y mi sueldo es %.2f"%persona
print(mensaje_con_formato_2)

# Primer formato 2:
mensaje_con_formato_2="Hola mi nombre es %s y mi apellido es %s y mi sueldo es %.2f"
print(mensaje_con_formato_2%persona)


# Uso del método format en python

# 1 primera forma
nombre="Fabricio"
edad=29
sueldo=3000
mensaje_con_formato="Nombre {} Edad: {} Sueldo: {:.2f}".format(nombre,edad,sueldo)

print(mensaje_con_formato)


# 2 segunda forma

mensaje='Nombre {0} Edad: {1} Sueldo: {2:.2f}'.format(nombre,edad,sueldo)

# print(mensaje)

# 3 tercera forma

mensaje='Sueldo {2:.2f} Edad: {1} Nombre: {0}'.format(nombre,edad,sueldo)

print(mensaje)


# 4 cuarta forma

mensaje="Nombre {n} Edad {e} Sueldo {s:.2f} ".format(n=nombre,e=edad,s=sueldo)

print(mensaje)

# 5 Quinta forma 

diccionario={'nombre':"Ivan",
             'edad':45,
             'sueldo':8000.00}

mensaje="Nombre {persona[nombre]} Edad {persona[edad]} Sueldo {persona[sueldo]:.2f}".format(persona=diccionario)

print(mensaje)


# 6 Sexta Forma

# Uso de f-string (Template Literal)


mensaje=f"Nombre {nombre} Edad {edad} Sueldo {sueldo:.2f}"
print(mensaje)



# Método print, (sep separa las cadenas)
print(nombre,edad,sueldo,sep='-')



# Multiplicacion de cadenas(str) en python

res=5*"Hola"

print(res)

# Multiplicacion de tuplas

res=5*("Hola","Mundo")
print(f"Tupla veces: {res}")



# Multiplicacion de listas

res=10*[0]

print(f"Lista veces: {res}")




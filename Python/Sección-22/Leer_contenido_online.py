
from urllib.request import urlopen


# Leer el contenido online

# with urlopen('http://globalmentoring.com.mx/recuros/GlobalMentoring.txt') as mensaje:
# #   contenido=mensaje.read()    
#   contenido=mensaje.read().decode('UTF-8')
#   print(contenido)

with open('pythonIA.txt','r',encoding='UTF-8') as archivo:
    contenido=archivo.read()


# Otros métodos de la clase (str)

# Contar ocurrencia de una cadena de otra

print(contenido.count('Python'))

# Método replace y strip, reemplazar contenido en un string

print(contenido.replace(' ','-'))



# Método upper

# print(contenido.upper())

# # Método lower

# print(contenido.lower())


# Vamos a preguntas si esta cadena existe

# print('python'.lower() in contenido.lower())


# srtatswith - inica con
print('Inicia con',contenido.startswith('P'))

# endswith - termina con
print('Termina con',contenido.upper().endswith(' lenguaje natural.'.upper()))


# Funciones islower y isupper en python, significan los dos si contiene todos los caracteres en minisculas(islower) y mayusculas(isupper)

mensaje='Hola Mundo'
print(mensaje.lower().islower())
print(mensaje.upper().isupper())








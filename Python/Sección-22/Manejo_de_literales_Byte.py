# Manejo de Literales de tipo Byte en python



# Caracteres en bytes

caracteres_en_bytes=b"Hola Mundo"
print(caracteres_en_bytes)


mensaje=b"Universidad Python"

print(mensaje[0])

print(chr(mensaje[0]))


lista_caracteres=mensaje.split()
print(lista_caracteres)


# Convertir de str a bytes y viceversa

string = 'Programación con Python'

print(f'String original {string}')

# Lo que hace el método encode que codifica una cadena para convertirla en otro tipo de dato

# Convertir en string a bytes usando encode

bytes=string.encode('UTF-8')

print(f"Bytes codificado: {bytes}")

# Convertir en bytes a string usando decode

#Lo que hace el método decode que decodifca una cadena para conrvetirla en el mismo tipo de dato que tenia 

string2=bytes.decode('UTF-8')

print(f"String decodificado: {string2}")



print(string == string2)

# Center - Centrar un str

titulo="Sitio Web official N1ckweb"


# print(titulo.center(50,'*'))
# print(len(titulo.center(50,'*')))

print(titulo.center(len(titulo)+10,'-'))


# Alineado a la izquierda con el método (ljust) justifica a la izquierda

print(titulo.ljust(50,'/'))

print(titulo.ljust(len(titulo)+10,'-'))



# Alineado a la derecha con el método (rjust) justifica a la derecha

print(titulo.rjust(50,'*'))

print(titulo.rjust(len(titulo)+10,'-'))


# Eliminar caracteres al inicio y final de una cadena

titulo1='*** PythoIADataScients.com *** ' 
print(f'Cadena original: {titulo1} {len(titulo1)}')

# El método strip() quita los espacios en blanco al inicio de la cadena y al final

titulo1=titulo1.strip()
print(f"Cadena modificada {titulo1} {len(titulo1)}")

titulo1='***PythoIADataScients.com***'.strip('*')
print(titulo1) 

# Quita lo espacio en blanco de la izquierda con (lstrip())
titulo1='***PythoIADataScients.com***'.lstrip('*')
print(titulo1)

# Quita lo espacio en blanco de la derecha con (rstrip())
titulo1='***PythoIADataScients.com***'.rstrip('*')
print(titulo1)

# Forma de quitarlo sin usar cada método del lado derecho y izquierdo
titulo1='*** PythoIADataScients.com *** '.strip().strip('*').strip('*')

print(titulo1)
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



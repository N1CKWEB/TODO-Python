
# Lectura de archivos en python


try:
  # archivo=open("c:\\RUTA DE PYTHON DEVELOPER\\Python\\Sección-15\\prueba.txt","r")
  archivo=open("prueba.txt","r",encoding="UTF-8")
  #Leer algunos caracteres
  # print(archivo.readlines(7))
except Exception as e:
  print(f'Ocurrio un error: {e}')
finally:
  print('La prueba de archivo ha finalizado!!')


# Más formas de trabajar con archvios en python

# Iterar el archivo

# for linea in archivo:
#   print(linea)


# Leer lineas
# print(archivo.readlines())


# Acceder solo a una linea
# print(archivo.readlines()[2])


# Abrimos o copiamos un archivo y crear uno nuevo

# a - enexar información

# archivo2=open("copia.txt","a")
# archivo2.write(archivo.read())







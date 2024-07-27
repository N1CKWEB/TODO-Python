

# Manejo de archivos en python

# Estas es la forma de crear un archivo en python, y para abrirlo también

# Especificar el juego de caracteres de un archivo de Texto
try:
  archivo = open('prueba.txt','w',encoding='UTF-8')
  archivo.write("Agregamos información al archivo en VSCode\n")
  archivo.write("Adíos!!")
except Exception as e:
  print(f'Ocurrio un error: {e}')
finally:
  archivo.close()
  print("Fin del archivo")
#   archivo.write("Nueva info")












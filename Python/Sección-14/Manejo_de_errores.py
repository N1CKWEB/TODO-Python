from test_de_manejos_de_errores import NumerosIdenticosException
# Manejo de errores o excepciones en python,para el manejo de errores acá en python utilizamos try/except es lo mismo que el trycatch conocido en otros lenguajes es para manejar errores en python.

# La clase de error de menor jerarquia va primero que clases padres con mayor jerarquia para ejecutarlas a las excepciones


try:
  10/0
except ZeroDivisionError as e:
  print(f'Ocurrio un error: {e}')


# Procesamiento de Excepciones 

resultado=None


# Procesar clases de excepción más específicas


# Bloques else y finally al manejar excepciones, finally siempre se va a ejecutar esta excepción ya sea si arroja una excepción o da un resultado correcto.

#La palabra reservada "raise" nos permite lanzar o arrojar una excepción

try:
  a=int(input("Primer número: "))
  b=int(input("Segundo número:"))
  if a==b:
    raise NumerosIdenticosException("Números identicos")    
  resultado=a/b
  print(resultado)
except ZeroDivisionError as e:
   print(f'Ocurrio un error: {e} , {type(e)}')
except TypeError as ty:
   print(f"Ocurrio un error: {ty}, {type(ty)}") 
except ValueError as vl:
    print(f"Ocurrio un error: {vl}, {type(vl)}")
except Exception as ex:
    print(f"Ocurrio un error: {ex}, {type(ex)}")
else:
    print("No se arrojo ninguna excepción!")
finally: 
     print("Ejecución de bloque finally!!!")
     
print(f"Resultado:{resultado}")
print("Continuamos....")














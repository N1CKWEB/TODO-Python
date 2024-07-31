
# Un cursor nos permite ejecutar sentencia SQL en postgreSQL 
import psycopg2

conexion = psycopg2.connect(
    user='postgres1',
    password='admin', 
    host='127.0.0.1',
    port='5432',
    database='test_db'
    )


# Función fetch all en Pyscopg
try:
     with conexion:
      with conexion.cursor() as cursor:
       sentencia="DELETE FROM persona WHERE id_persona IN %s "
       entrada=input("Proporciona los id personas a (eliminar): ")
       valores=(tuple(entrada.split(",")),)
       cursor.execute(sentencia,valores)
     #   conexion.commit() #Guarda los cambios en la BD
       registros_actualizados=cursor.rowcount
       print(f"Registros eliminados: {registros_actualizados}") 
         
     #   sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
     #   entrada = input("Proporciona los id\'s a buscar (separados por comas): ")
     #   llaves_primarias=(tuple(entrada.split(',')),)
     # #   id_persona = input("Proporciona el valor id_persona: ")
     #   cursor.execute(sentencia,llaves_primarias)
     # # Acá recuperamos todos los registros con esta sentencia
     # #   registros = cursor.fetchall() #este metodo recupera todos los  registros que se han recuperado
     #   registros=cursor.fetchall() #Lo que hace que recuperar solo un registro de lo pedido
     #   for registro in registros:
     #        print(registros)   
     #   print(registros) 
     
except Exception as e:
     print(f'Ocurrio un error {e}')
finally:     
     conexion.close()
  
# Rollback significa dar vuelta atras a todos los cambios que se allan hecho
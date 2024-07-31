
# Un cursor nos permite ejecutar sentencia SQL en postgreSQL 
import psycopg2 as bd

conexion = bd.connect(
    user='postgres',
    password='admin', 
    host='127.0.0.1',
    port='5432',
    database='test_db'
    )


# Función fetch all en Pyscopg
try:
    #  conexion.autocommit = False  #No es buena prácticas aplicar esto  
     with conexion:
         with conexion.cursor() as cursor:
          sentencia='INSERT INTO persona(nombre,apellido,edad,email) VALUES (%s,%s,%s,%s)'
          valores=("Marck","Zuckerberg",40,"zuckpython@gmail.com")
          
          cursor.execute(sentencia,valores)
          
          sentencia2="UPDATE persona SET nombre = %s , apellido = %s , edad = %s, email = %s WHERE id_persona = %s"
          valores2=("Elon","Musk",53,"muskteslasolar@gmail.com",21)
          
          cursor.execute(sentencia2,valores2)
            
          print("Termina la transación, se hizo commit!")
except Exception as e:
     conexion.rollback()
     print(f'Ocurrio un error, se hizo roolback {e}')
finally:     
     conexion.close()
  
# Rollback significa dar vuelta atras a todos los cambios que se allan hecho















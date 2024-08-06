from psycopg2 import pool
from Logger_base import log
import sys

class Conexion:
    
    _DATABASE = "test_db"
    _USERNAME = "postgres"    
    _PASSWORD = "admin"    
    _DB_PORT = "5432"
    _HOST = "127.0.0.1"
    _MIN_CONEXIONES=1
    _MAX_CONEXIONES=5
    _pool=None #Es un objeto que va administrar a sus ojectos de conexion hacia a la BD 
    
    @classmethod
    def obtener_poll(cls):
       if cls._pool is None:
         try:
           cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CONEXIONES,
                    cls._MAX_CONEXIONES, 
                    host=cls._HOST,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    port=cls._DB_PORT,
                    database=cls._DATABASE 
                    )
           log.debug(f"Creacion del pool exitosa {cls._pool}")
           return cls._pool
         except Exception as e:
           log.debug(f'Ocurrio un error al obtener el pull: {e}')
           sys.exit()
       else:
           return cls._pool    
         
         
    @classmethod
    def obtener_conexion(cls):
      conexion=cls.obtener_poll().getconn()
      log.debug(f"Conexion obtenida del pool {conexion}")
      return conexion
    
    
    @classmethod
    def liberar_conexion(cls,conexion):
      cls.obtener_poll().putconn(conexion)
      log.debug(f"Regresamos la conexion al poll: {conexion}") 
      
    @classmethod
    def cerrar_conexion(cls):
      cls.obtener_poll().closeall()
 
    @classmethod
    def obtener_cursor(cls):
      pass
           
    # @classmethod
    # def cerrar(cls):
    #     pass      
    
    
if __name__ == "__main__":
  conexion01=Conexion.obtener_conexion()
  Conexion.liberar_conexion(conexion01)
  conexion02=Conexion.obtener_conexion() 
  conexion03=Conexion.obtener_conexion()
  Conexion.liberar_conexion(conexion03)  
  conexion04=Conexion.obtener_conexion() 
  conexion05=Conexion.obtener_conexion()
  Conexion.liberar_conexion(conexion05)  
   
   
   
   
  
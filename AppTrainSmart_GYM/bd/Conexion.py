from psycopg2 import pool
from Logger_base import log
import sys

class Conexion:
    
    _DATABASE = "AppTrainSmart"
    _USERNAME = "postgres"
    _PASSWORD = "admin"
    _DB_PORT = "5432"
    _HOST = "127.0.0.1"
    _MIN_CONEXIONES = 1
    _MAX_CONEXIONES = 5
    _pool = None 
    
    @classmethod
    def obtener_pool(cls):
        if cls._pool is None:
            try:
                log.debug("Intentando crear el pool de conexiones")
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CONEXIONES,
                    cls._MAX_CONEXIONES,
                    host=cls._HOST,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    port=cls._DB_PORT,
                    database=cls._DATABASE
                )
                log.debug(f'Creación del pool exitosa {cls._pool}')
            except Exception as e:
                log.error(f'Ocurrió un error al crear el pool de conexiones: {e}')
                sys.exit()  # Detener el programa si hay un error
        return cls._pool  # Devolver el pool creado o existente
    
    @classmethod
    def obtener_conexion(cls):
        conexion = cls.obtener_pool().getconn()  # Obtener conexión del pool
        log.debug(f"Conexión obtenida del pool {conexion}")
        return conexion    
    
    @classmethod
    def liberar_conexion(cls, conexion):
        cls.obtener_pool().putconn(conexion)  # Regresar la conexión al pool
        log.debug(f"Regresamos la conexión al pool: {conexion}")
      
    @classmethod
    def cerrar_conexion(cls):
        cls.obtener_pool().closeall()  # Cerrar todas las conexiones del pool

if __name__ == "__main__":
    conexion01 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion01)
    conexion02 = Conexion.obtener_conexion() 
    conexion03 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion03)  
    conexion04 = Conexion.obtener_conexion() 
    conexion05 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion05)

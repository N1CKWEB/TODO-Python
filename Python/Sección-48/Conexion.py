from psycopg2 import pool
from Logger_base import log
import sys

class Conexion:
    
    _DATABASE = "AppZonaFitGym"
    _USERNAME = "postgres"    
    _PASSWORD = "admin"    
    _DB_PORT = "5432"
    _HOST = "127.0.0.1"
    _MIN_CONEXIONES = 1
    _MAX_CONEXIONES = 5
    _pool = None  # Es un objeto que va a administrar a sus objetos de conexión hacia la BD 
    
    @classmethod
    def obtener_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CONEXIONES,
                    cls._MAX_CONEXIONES,
                    host=cls._HOST,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    port=cls._DB_PORT,  # Coma agregada
                    database=cls._DATABASE
                )
                log.debug(f'Creación del pool exitosa {cls._pool}')
            except Exception as e:
                log.error(f'Ocurrió un error al crear el pool de conexiones: {e}')
                sys.exit()
        return cls._pool
    
    @classmethod
    def obtener_conexion(cls):
        conexion = cls.obtener_pool().getconn()  # Aquí se corrigió el llamado del método
        log.debug(f"Conexión obtenida del pool {conexion}")
        return conexion    
    
    @classmethod
    def liberar_conexion(cls, conexion):
        cls.obtener_pool().putconn(conexion)  
        log.debug(f"Regresamos la conexión al pool: {conexion}")
      
    @classmethod
    def cerrar_conexion(cls):
        cls.obtener_pool().closeall()

if __name__ == "__main__":
    conexion01 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion01)
    conexion02 = Conexion.obtener_conexion() 
    conexion03 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion03)  
    conexion04 = Conexion.obtener_conexion() 
    conexion05 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion05)

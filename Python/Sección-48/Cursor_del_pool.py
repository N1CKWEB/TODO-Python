
from Logger_base import log
from Conexión import Conexion


class CursorDelPool:
    
    def __init__(self, ):
      self.conexion= None
      self.cursor = None
      
    
    def __enter__ (self):
        log.debug('Inicio del metodo __enter__')
        self._conexion=Conexion.obtener_conexion()
        self._cursor=self._conexion.cursor()
        return self._cursor
    
    def __exit__ (self,tipo_excepcion,valor_excepcion,detalle_excepcion):
        log.debug('Se ejecuta metodo __exit__')
        if valor_excepcion:
            self._conexion.rollback()
            log.error(f'Ocurrio una excepcion, se hace roolback:
                      {valor_excepcion} {tipo_excepcion} {detalle_excepcion}') 
        else:
            self._conexion.commit()
            log.debug('Commit de la transaccion!')
            
        self._cursor.close()
        Conexion.liberar_conexion(self._conexion)
        
        
if __name__ == "__main__":
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')                  
        cursor.execute("SELECT * FROM Cliente")
        log.debug(cursor.fetchall())
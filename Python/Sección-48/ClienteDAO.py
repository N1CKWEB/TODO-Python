from Conexion import Conexion
from Cursor_del_pool import CursorDelPool
from Cliente import Cliente
from Logger_base import log

class ClienteDAO_NEW:
    _SELECCIONAR = "SELECT * FROM cliente ORDER BY id_cliente"
    _INSERTAR = "INSERT INTO cliente(nombre, apellido, membresia) VALUES (%s, %s, %s)"
    _ACTUALIZAR = "UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id_cliente=%s"
    _ELIMINAR = "DELETE FROM cliente WHERE id_cliente=%s"

    @classmethod
    def seleccionar_bd(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes

    @classmethod
    def insertar_bd(cls, cliente):
        with CursorDelPool() as cursor:
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f"Cliente insertado: {cliente}")
            return cursor.rowcount

    @classmethod
    def actualizar_bd(cls, cliente):
        with CursorDelPool() as cursor:
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id_cliente)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f"Cliente actualizado: {cliente}")
            return cursor.rowcount

    @classmethod
    def eliminar_bd(cls, cliente):
        with CursorDelPool() as cursor:
            cursor.execute(cls._ELIMINAR, (cliente.id_cliente,))
            log.debug(f"Cliente eliminado con id: {cliente.id_cliente}")
            return cursor.rowcount

if __name__ == "__main__":

    # Insertar cliente
    usuario02 = Cliente(id_cliente=2, nombre='Juan', apellido='Martinez', membresia='2203')
    usuario_insertado = ClienteDAO_NEW.insertar_bd(usuario02)
    usuario03 = Cliente(id_cliente=3, nombre='Naim', apellido='Ramirez', membresia='2104')
    usuario_insertado = ClienteDAO_NEW.insertar_bd(usuario03)
    usuario04 = Cliente(id_cliente=4, nombre='Nacho', apellido='Borcia', membresia='2305')
    usuario_insertado = ClienteDAO_NEW.insertar_bd(usuario04)
    
    
    
    
    
    
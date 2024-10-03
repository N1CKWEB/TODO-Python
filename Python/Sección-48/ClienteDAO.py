from Conexion import Conexion
from Cursor_del_pool import CursorDelPool
from Cliente import Cliente
from Logger_base import log


class ClienteDAO:

    _SELECCIONAR = "SELECT * FROM cliente ORDER BY id_cliente"
    _INSERTAR = "INSERT INTO Cliente(nombre, apellido, membresia) VALUES (%s, %s, %s)"
    _ACTUALIZAR = "UPDATE Cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id_cliente=%s"
    _ELIMINAR = "DELETE FROM Cliente WHERE id_cliente=%s"

    # Seleccionar BD
    @classmethod
    def seleccionar_bd(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2])
                clientes.append(cliente)
            return clientes

    # Insertar BD
    @classmethod
    def insertar_bd(cls, cliente):
        with CursorDelPool() as cursor:
            valores = (cliente._nombre, cliente._apellido, cliente._membresia)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f"Cliente insertado: {cliente}")
            return cursor.rowcount

    # Actualizar BD
    @classmethod
    def actualizar_bd(cls, cliente):
        with CursorDelPool() as cursor:
            valores = (cliente._nombre, cliente._apellido, cliente._membresia, cliente._id_cliente)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f"Cliente actualizado: {cliente}")
            return cursor.rowcount

    # Eliminar BD
    @classmethod
    def eliminar_bd(cls, cliente):
        with CursorDelPool() as cursor:
            cursor.execute(cls._ELIMINAR, (cliente._id_cliente,))
            log.debug(f"Cliente eliminado con id: {cliente._id_cliente}")
            return cursor.rowcount


if __name__ == "__main__":
    # Insertar cliente
    usuario01 = Cliente(id_cliente=1, nombre='Nicolas', apellido='Diaz', membresia=2303)
    usuario_insertado = ClienteDAO.insertar_bd(usuario01)
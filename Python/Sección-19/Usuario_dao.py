from Conexion import Conexion
from Cursor_del_pool import CursorDelPool
from Usuario import Usuario
from Logger_base import log

class UsuarioDAO:

    _SELECCIONAR = "SELECT * FROM usuario ORDER BY id_usuario"
    _INSERTAR = "INSERT INTO usuario(username, password) VALUES (%s, %s)"
    _ACTUALIZAR = "UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s"
    _ELIMINAR = "DELETE FROM usuario WHERE id_usuario=%s"

    @classmethod
    def seleccionar_bd(cls):
        with CursorDelPool() as cursor:
            log.debug("Seleccionando usuarios")
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar_bd(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f"Usuario a insertar: {usuario}")
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount

    @classmethod
    def actualizar_bd(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f"Usuario actualizado: {usuario}")
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount

    @classmethod
    def eliminar_bd(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f"Usuario eliminado con id: {usuario.id_usuario}")
            cursor.execute(cls._ELIMINAR, (usuario.id_usuario,))
            return cursor.rowcount

if __name__ == "__main__":
    usuario03 = Usuario(username="Michael", password="MichaelLB23")
    usuarios_insertadas = UsuarioDAO.insertar_bd(usuario03)
    log.debug(f"usuarios insertadas: {usuarios_insertadas}")

    usuario03 = Usuario(3, "SergioDiaz31", "3101")
    usuarios_actualizadas = UsuarioDAO.actualizar_bd(usuario03)
    log.debug(f"usuarios actualizadas: {usuarios_actualizadas}")

    usuario01 = Usuario(id_usuario=2)
    usuarios_eliminadas = UsuarioDAO.eliminar_bd(usuario01)
    log.debug(f"usuarios eliminadas: {usuarios_eliminadas}")

    usuarios = UsuarioDAO.seleccionar_bd()
    for usuario in usuarios:
        log.debug(usuario)

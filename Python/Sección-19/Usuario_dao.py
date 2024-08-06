from Conexion import Conexion
from Cursor_del_pool import CursorDelPool     
from Usuario import Usuario
from Logger_base import log

class UsuarioDAO():
    
    _SELECCIONAR = "SELECT * FROM usuario ORDER BY id_usuario"
    _INSERTAR = "INSERT INTO usuario(username, password) VALUES (%s, %s)"
    _ACTUALIZAR = "UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s"
    _ELIMINAR = "DELETE FROM usuario WHERE id_usuario=%s"
    
    # Seleccionar BD
    @classmethod   
    def seleccionar_bd(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0],registro[1],registro[2])
                usuarios.append(usuario)
            return usuarios

    # Insertar BD
    @classmethod   
    def insertar_bd(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario._username, usuario._password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f"usuario insertado: {usuario}")
            return cursor.rowcount
      
    # Actualizar BD
    @classmethod   
    def actualizar_bd(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario._username, usuario._password,usuario._id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f"usuario actualizado: {usuario}")
            return cursor.rowcount
     
    # Eliminar BD
    @classmethod   
    def eliminar_bd(cls, usuario):
        with CursorDelPool() as cursor:
            cursor.execute(cls._ELIMINAR, (usuario._id_usuario,))
            log.debug(f"usuario eliminado con id: {usuario._id_usuario}")
            return cursor.rowcount

if __name__ == "__main__":
    
   #  # Insertar un registro
   #  usuario01 = Usuario(username="nicholas23", password="123456")
   #  usuarios_insertadas = UsuarioDAO.insertar_bd(usuario01)
   #  log.debug(f"usuarios insertadas: {usuarios_insertadas}")
    
   #  Actualizar registro
   #  usuario01 = Usuario(2,"zuck03", "12344555")
   #  usuarios_actualizadas = UsuarioDAO.actualizar_bd(usuario01)
   #  log.debug(f"usuarios actualizadas: {usuarios_actualizadas}")
    
   # #  Eliminar registro
   #  usuario01 = Usuario(id_usuario=1)
   #  usuarios_eliminadas = UsuarioDAO.eliminar_bd(usuario01)
   #  log.debug(f"usuarios eliminadas: {usuarios_eliminadas}")
    
    # Seleccionar objetos
    usuarios = UsuarioDAO.seleccionar_bd()
    for usuario in usuarios:
        log.debug(usuario)

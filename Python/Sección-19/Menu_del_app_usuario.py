from Conexion import Conexion
from Cursor_del_pool import CursorDelPool
from Usuario import Usuario
from Logger_base import log
from Usuario_dao import UsuarioDAO

opcion = None

while opcion != 5:
    try:
        print("Opciones: ")
        print("1-Listar Usuario")
        print("2-Agregar Usuario")
        print("3-Actualizar Usuario")
        print("4-Eliminar Usuario")
        print("5-Salir")
        opcion = int(input("Escribe tu opcion (1-5): "))

        if opcion == 1:
            usuarios = UsuarioDAO.seleccionar_bd()
            for usuario in usuarios:
                log.info(usuario)

        elif opcion == 2:
            username_var = input("Introduce el usuario: ")
            password_var = input("Introduce la contraseña: ")
            usuario = Usuario(username=username_var, password=password_var)
            usuarios_insertados = UsuarioDAO.insertar_bd(usuario)
            log.info(f"Usuarios insertados: {usuarios_insertados}")

        elif opcion == 3:
            id_usuario_var = int(input("Introduce el id del usuario: "))
            username_var = input("Introduce el nuevo nombre de usuario: ")
            password_var = input("Introduce la nueva contraseña: ")
            usuario = Usuario(id_usuario_var, username_var, password_var)
            usuarios_actualizados = UsuarioDAO.actualizar_bd(usuario)
            log.info(f"Usuarios actualizados: {usuarios_actualizados}")

        elif opcion == 4:
            id_usuario_var = int(input("Introduce el id del usuario: "))
            usuario = Usuario(id_usuario=id_usuario_var)
            usuarios_eliminados = UsuarioDAO.eliminar_bd(usuario)
            log.info(f"Usuarios eliminados: {usuarios_eliminados}")

    except Exception as e:
        print(f'Ocurrio un error: {e}')

print('Salimos del programa...')

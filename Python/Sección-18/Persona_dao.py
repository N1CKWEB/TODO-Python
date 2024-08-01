# Realizando un CRUD, DAO (Data Access Object)

# DAO es un patron de diseño para comunicarse con la BD

from Conexion import Conexion
from Persona import Persona
from Logger_base import log


class PersonaDAO():
    
    _SELECCIONAR = "SELECT * FROM persona ORDER BY id_persona"
    _INSERTAR = "INSERT INTO persona(nombre, apellido, edad, email) VALUES (%s, %s, %s, %s)"
    _ACTUALIZAR = "UPDATE persona SET nombre=%s, apellido=%s, edad=%s, email=%s WHERE id_persona=%s"
    _ELIMINAR = "DELETE FROM persona WHERE id_persona=%s"
    
    # Seleccionar BD
    @classmethod   
    def seleccionar_bd(cls):
        with Conexion.obtener_conexion() as conexion: 
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []
                for registro in registros:
                    persona = Persona(registro[0], registro[1], registro[2], registro[3], registro[4])
                    personas.append(persona)
                return personas

    # Insertar BD
    @classmethod   
    def insertar_bd(cls, persona):
        with Conexion.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (persona._nombre, persona._apellido, persona._edad, persona._email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f"Persona insertada: {persona}")
                return cursor.rowcount
      
    # Actualizar BD
    @classmethod   
    def actualizar_bd(cls, persona):
        with Conexion.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (persona._nombre, persona._apellido, persona._edad, persona._email, persona._id_persona)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f"Persona actualizada: {persona}")
                return cursor.rowcount
     
    # Eliminar BD
    @classmethod   
    def eliminar_bd(cls, persona):
        with Conexion.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._ELIMINAR, (persona._id_persona,))
                log.debug(f"Persona eliminada con id: {persona._id_persona}")
                return cursor.rowcount

if __name__ == "__main__":
    # Insertar un registro
    # persona01 = Persona(nombre="Sam", apellido="Altman", edad=39, email="openai@gmail.com")
    # personas_insertadas = PersonaDAO.insertar_bd(persona01)
    # log.debug(f"Personas insertadas: {personas_insertadas}")
    
    # Actualizar registro
    # persona01 = Persona(1, "Mariela", "Garrido", 49, "marielagarrido@gmail.com")
    # personas_actualizadas = PersonaDAO.actualizar_bd(persona01)
    # log.debug(f"Personas actualizadas: {personas_actualizadas}")
    
    # Eliminar registro
    persona01 = Persona(id_persona=28)
    personas_eliminadas = PersonaDAO.eliminar_bd(persona01)
    log.debug(f"Personas eliminadas: {personas_eliminadas}")
    
    # Seleccionar objetos
    personas = PersonaDAO.seleccionar_bd()
    for persona in personas:
        log.debug(persona)


# Manejo de un Pool de conexiones 


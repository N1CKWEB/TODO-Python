import logging as log

# Handler = Manejador es un recurso a donde vamos a mandar esta información

log.basicConfig(level=log.DEBUG,
                format="%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s ",
                datefmt="%I:%M:%S",
                handlers=[
                            log.FileHandler('capa_datos.log'),
                            log.StreamHandler()
                ])



if __name__ == "__main__":
 log.debug("Mensaje a nivel de debug")
 log.info("Mensaje a nivel de info")
 log.warning("Mensaje a nivel de warning")
 log.error("Mensaje a nivel de error")
 log.critical("Mensaje a nivel de critical")



















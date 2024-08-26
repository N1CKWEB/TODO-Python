


# Acceso de atributos en python


#Ejemplo atributos (públicos,protegidos y privados) 

class MiClase:
  
  def __init__(self,publico,protegido,privado) -> None:
    self.publico=publico
    self._protegido=protegido
    self.__privado=privado
    
  def __repr__(self) -> str:
    return f""

  
objecto = MiClase("Valor Publico ","Valor protegido","Valor privado")    

# Acceso al atributo público

print(objecto.publico)


# Modificar el valor público
objecto.publico="Nuevo valor publico"
print(objecto.publico)



# Acceso al valor protegido
# Esta práctica esta mal, solo debemos usar un valor protegido dentro de la misma clase a clases hijas
print(objecto._protegido)
objecto._protegido="Nuevo valor protegido"
print(objecto._protegido)



# Acceso al valor privado
# print(MiClase.__privado) De esta forma no se puede acceder a un valor privado , pero convierte: objeto._clase__.__atributo__privado
print(objecto._MiClase__privado) #Forma única para acceder a un valor privado
# Modificar este valor de privado
objecto._MiClase__privado="Nuevo valor privado" #Forma única para modificar valor privado
print(objecto._MiClase__privado) 






from Logger_base import log


class Usuario:
    def __init__(self, id_usuario=None, username=None, password=None):
      self._id_usuario = id_usuario
      self._username = username
      self._password = password
      
      
    #GET y SET
    
    @property
    def id_usuario(self):
        return self._id_usuario
    
    @id_usuario.setter
    def id_usuario(self,id_usuario):
        self._id_usuario=id_usuario
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self,username):
        self.username=username
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self,password):
        self._password=password
        
    
    #Método str()
    
    def __str__(self) -> str:
        return f"Usuario: [ID: {self._id_usuario} Username: {self._username} Password: {self._password}]"
    
     
     
if __name__ == "__main__":    
 usuario01=Usuario(1,"Nick2313","231310095")
 log.debug(usuario01)

 # Simular un insert
 usuario02=Usuario(2,"JuanMartinez03","030401") 
 log.debug(usuario02)

# # Simular un delete
# usuario01=Usuario(id_persona=1)
# log.debug(usuario01)
     
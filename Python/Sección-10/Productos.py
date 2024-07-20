# Diseño de clases en python
 
class Producto:
     
     contador_productos = 0
     
     @classmethod
     def _contador_estatico_produ(cls):
         cls.contador_productos += 1
         return cls.contador_productos
             
     def __init__(self, nombre,precio):
       self._id_productos = Producto._contador_estatico_produ() 
       self._nombre = nombre
       self._precio = precio 
       
       
     #GET y SET
     @property
     def id_produtos(self):
         return self._id_produtos 
    
     @id_produtos.setter
     def id_produtos (self,id_produtos):
         self._id_produtos=id_produtos
     
     @property
     def nombre(self):
         return self._nombre 
    
     @nombre.setter
     def nombre (self,nombre):
         self._nombre=nombre 
     
     @property
     def precio(self):
         return self._precio 
    
     @precio.setter
     def precio (self,precio):
         self._precio=precio
         
   
    #Método str
    
     def __str__(self) -> str:
         return f"Producto: [ID Producto: {self._id_productos} , Nombre: {self._nombre} , Precio: {self._precio}]"
     
   
   
if __name__ == "__main__":
    Producto1= Producto("Camisa",100.00)
    print(Producto1)   
    Producto2= Producto("Pantalon Oversize",250000.00)
    print(Producto2)   
      


      
      
      
      
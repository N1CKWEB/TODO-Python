from Productos import Producto

class Orden:

    contador_ordenes = 0

    @classmethod
    def contador_estatico_orden(cls):
        cls.contador_ordenes += 1
        return cls.contador_ordenes
        
    def __init__(self, productos):
        self._id_orden = Orden.contador_estatico_orden()
        self._productos = list(productos)
      
    # GET y SET
    @property
    def id_orden(self):
        return self._id_orden
    
    @id_orden.setter
    def id_orden(self, id_orden):
        self._id_orden = id_orden
    
    @property
    def productos(self):
        return self._productos
    
    @productos.setter
    def productos(self, productos):
        self._productos = productos
             
    
    def agregar_producto(self, producto):
        self._productos.append(producto)
      
    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total
       
    def __str__(self) -> str:
        productos_str = ""
        for producto in self._productos:
            productos_str += producto.__str__() + "|"           
        return f"Orden: [ID: {self._id_orden} , \n Productos: {productos_str}]"

if __name__ == "__main__":
    producto1 = Producto("Camisa", 100.00)
    producto2 = Producto("Pantalon Oversize", 250000.00)
    productos1 = [producto1, producto2]
    orden1 = Orden(productos1)
    print(orden1)
    orden2 = Orden(productos1)
    print(orden2)
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
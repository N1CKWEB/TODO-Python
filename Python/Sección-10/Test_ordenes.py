from  Productos import Producto
from  Orden import Orden




producto1 = Producto("Camisa", 100.00)
producto2 = Producto("Pantalon Oversize", 250000.00)
producto3 = Producto("Lenovo IDEAPAD GAMING 3",1350000.00)
producto4 = Producto("Zapatillas Nike ",125000.00)


productos1 = [producto1, producto2]
productos2 = [producto3, producto4]

orden1 = Orden(productos1)
orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)
print(orden1)
print(f"El total de la orden 1 es: {orden1.calcular_total()}")
orden2 = Orden(productos2)
orden2.agregar_producto(producto1)
orden2.agregar_producto(producto2)
print(orden2)
print(f"El total de la orden 2 es: {orden2.calcular_total()}")
      
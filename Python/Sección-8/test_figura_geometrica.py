from Cuadrado import *
from Rectangulo import *


print("Creacion objeto cuadrado".center(50,"-"))

cuadrado1=Cuadrado(lado=5,color='Rojo')
cuadrado1.alto=9
cuadrado1.ancho=9
print(f'Calculo area de cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)


print("Creacion objeto rectangulo".center(50,"-"))

rectangulo1=Rectangulo(ancho=9,alto=8,color="Azul")
rectangulo1.ancho=15
print(f'Calculo area de rectangulo {rectangulo1.calcular_area()}')
print(rectangulo1)



# MRO - Method Resolution Order
print(Cuadrado.mro())














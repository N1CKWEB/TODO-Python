# Clases y Objetos en python 

# Parametro self, es una referencia al objeto en si mismo, que se va agregar a la clase

# Se llama el método init o método underco
class Persona:
  # Robusteciendo el método init
   def __init__(self, nombre,apellido,edad,*valores,**terminos):
     self.nombre = nombre
     self.apellido=apellido
     self.edad = edad 
     self.valores=valores
     self.terminos=terminos
  
   def mostrar_detalles(self):
     print(f"Persona: {self.nombre} {self.apellido} {self.edad}{self.valores} y {self.terminos}")
  
  # Destructor de objetos:
   def __del__(self):
    print(f"Persona: {self.nombre}")       
     



persona1 = Persona("Nicolas","Diaz",19,"12414324",2,m="manzana verde",n="Nico")

persona2= Persona("Mariela","Garrido",49)

persona3= Persona("Sergio","Diaz",49)

print(f" El nombre es: {persona1.nombre} y el apellido es:  {persona1.apellido} y su edad es: {persona1.edad}")

print(f"El nombres es: {persona2.nombre} y el apellido es:{persona2.apellido} y la edad es: {persona2.edad}")
  
print(f"El nombre es: {persona3.nombre} y el apellido es: {persona3.apellido} y su edad es: {persona3.edad}")

print(f"Los valore son: {persona1.valores} y los terminos son:{persona1.terminos}")

# Referencias de Memoria y ejecución Paso a Paso:

# Así es para modificar el valor del atributo
persona1.edad=21

print(f" El nombre es: {persona1.nombre} y el apellido es:  {persona1.apellido} y su edad es: {persona1.edad}")

persona1.mostrar_detalles()
persona2.mostrar_detalles()
persona3.mostrar_detalles()


print("\n")

# Más de self y atributos en Objetos

Persona.mostrar_detalles(persona1)


persona1.fecha_de_nacimiento="23/03/2005"

print(persona1.fecha_de_nacimiento)

print("\n")

# Ejercicio - Clase Aritmética

class Aritmetica:
 
 """
 Clase aritmetica para realizar las operaciones de sumar,restar,etc
 """
 
 def __init__(self, operandoA, operandoB):
   self.operandoA = operandoA 
   self.operandoB = operandoB
   
 def sumar(self):
   return self.operandoA + self.operandoB

 def restar(self):
   return self.operandoA - self.operandoB
 
 def multiplicar(self):
   return self.operandoA * self.operandoB
 
 def dividir(self):
   return self.operandoA / self.operandoB
 
 
 def potencia(self):
   return self.operandoA ** self.operandoB
 
 
 def divisionX2(self):
   return self.operandoA // self.operandoB
 
 
 def porciento(self):
   return self.operandoA % self.operandoB
 
 

aritmetica1 = Aritmetica(23,45)

print(aritmetica1.sumar())
print(aritmetica1.restar())   
print(aritmetica1.multiplicar())   
print(aritmetica1.dividir())   
print(aritmetica1.potencia())   
print(aritmetica1.divisionX2())   
print(aritmetica1.porciento())   
   
   
print("\n")
   
#Ejercicio - Laboratorio Rectángulo

# class Rectangulo:
#   def __init__(self, base,altura):
#    self.base = base
#    self.altura = altura

#   def calcular_rectangulo(self):
#    return self.base * self.altura



# base=int(input("Introduce la base: "))
# altura=int(input("Introduce la altura: "))

# rectangulo1=Rectangulo(base,altura)

# print(f"Area del rectangulo: {rectangulo1.calcular_rectangulo()}")


print("\n")

# Ejercicio - Laboratorio Cubo

# class Cubo:
#   def __init__(self, ancho,alto,profundidad):
#     self.ancho = ancho
#     self.alto = alto
#     self.profundidad = profundidad
  
#   def calcular_cubo(self):
#     return self.ancho * self.profundidad * self.alto
  
  
# ancho=int(input("Introduce el ancho: "))
# profundidad=int(input("Introduce la profundidad: "))
# alto=int(input("Introduce el alto: "))

# cubo1=Cubo(ancho,profundidad,alto)  
     
# print(f"El volumen final del cubo: {cubo1.calcular_cubo()}")  
     
     
     
# Encapsulamiento en python 

# El "_" significa que hacemos el atributo encapsulado que significa que ninguna otra clase puede acceder a nuestro atributo y el usar "__" significa que lo hace más restrigido y ya no se puede ni modificar el atributo

class Perro:
  def __init__(self, ladrar, comer):
    self._ladrar = ladrar
    self._comer = comer
    
# Decorador de property, indica que el método se va a recuperar, y lo que hace que solo se pueda acceder a traves del método nomas 


# Métodos get y set en python

# GET: Es para obtener / recuperar
# SET: Es para colocar / modificar

# Atributos read-only (sólo lectura)
  #GET
  @property
  def  ladrar(self):
     return self._ladrar
  
  #SET
  @ladrar.setter 
  def ladrar(self, ladrar):
     self._ladrar=ladrar
  
  #GET   
  @property  
  def  comer(self):
    return self._comer

  #SET
  @comer.setter
  def comer(self, comer):
    self._comer=comer   



perro1=Perro("Gua Gua","Comida de Perro")



if __name__ == "__main__":
  print(perro1.ladrar)
  perro1.ladrar="GUAAAAAAAAAAAAAAAA"
  print(perro1.ladrar)
  print(perro1.comer)
  perro1.comer="DOG CHOW"
  print(perro1.comer)



print(__name__)



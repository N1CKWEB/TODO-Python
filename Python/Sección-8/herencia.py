# Herencia en python
# La clase object es la clase padre de todas las clases en python, pero no es necesario agregarlo

class PersonaHumana:
    def __init__(self, nombre, edad):
      self._nombre = nombre
      self._edad = edad
    
    #Lo que estamos haciendo acá, es sobrescribir el método
    def __str__(self) -> str:
       return f"Persona:  {self.nombre} {self.edad}"
    
    #GET
    @property
    def nombre(self):
        return self._nombre
   
    @property
    def edad(self):
        return self._edad
    
    #SET
    @nombre.setter
    def nombre(self,nombre):
     self._nombre=nombre           

    @edad.setter
    def edad(self,edad):
     self._edad=edad           
 

class Empleado(PersonaHumana):
  def __init__(self,nombre,edad,sueldo):
    #Tenemos que llamar al constructor de la clase padre para poder acceder a los demas atributo de la clase padre, se hace así:
    super().__init__(nombre,edad)  
    self.sueldo =sueldo 
  
    #Lo que estamos haciendo acá, es sobrescribir el método
  def __str__(self) -> str:
   return f"Empleado: Sueldo: {self.sueldo}  {super().__str__()} "
        
      

empleado1=Empleado("Nicolas",19,5000)

print(f"El nombre es: {empleado1.nombre} y su edad es:{empleado1.edad} y su sueldo es: {empleado1.sueldo}")    


 

# Ejercicio - Herencia

class Vehiculo:
  def __init__(self,color,ruedas):
    self._color=color
    self._ruedas=ruedas
    
    # Método __str__ para representación del objeto
  def __str__(self) -> str:
     return f"Color: {self.color} ,  Ruedas: {self.ruedas}"           
  #GET
  @property
  def color(self):
      return self._color
    
  @property
  def ruedas(self):
      return self._ruedas
      
    #SET 
  @color.setter
  def color(self,color):
      self._color=color
    
  @ruedas.setter
  def ruedas(self,ruedas):
      self._ruedas=ruedas 

class Coche(Vehiculo):      
  def __init__(self,color,ruedas,velocidad):
   super().__init__(color,ruedas)
   self._velocidad=velocidad
     
# Método __str__ utilizando super
  def __str__(self) -> str:
      return f'{super().__str__()}, Velocidad (km/hr): {self.velocidad}'
    
  
  #GET
  @property
  def velocidad(self):
    return self._velocidad
  
  #SET  
  @velocidad.setter
  def velocidad(self,velocidad):
    self._velocidad=velocidad
       
class Bicicleta(Vehiculo):
  def __init__ (self,color,ruedas,tipo):
    super().__init__(color,ruedas)  
    self._tipo=tipo
    
  
  # Método __str__ utilizando super
  def __str__(self) -> str:
   return f'{super().__str__()}, Tipo: {self.tipo}'

   
  #GET
  @property
  def tipo(self):
    return self._tipo
  
  #SET
  @tipo.setter
  def tipo(self,tipo):
    self._tipo=tipo   
  
  

vehiculo1=Vehiculo("Azul y Rojo" ,ruedas = 6)

coche1=Coche("Azul",ruedas=4,velocidad=123)

bicicleta1=Bicicleta("Rojo",ruedas=2,tipo="Urbano")


print(vehiculo1)
print(coche1)
print(bicicleta1)



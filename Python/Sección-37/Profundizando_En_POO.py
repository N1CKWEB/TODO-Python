
# Profundizando en la Programación Orientada a Objeto



class Persona:
    contador_persona=0
    
    def __init__(self,nombre,apellido ):
      self._nombre=nombre
      self._apellido=apellido
   

        
#Mostrar los atributos de un objeto
persona1=Persona("Nicolas","Diaz")        
print(persona1.__dict__)         

# Crear un atributo al vuelo(en este momento)
print(persona1.contador_persona) #Accediendo al atributo de clases
# Pero no es posible modificarlo con en el objeto, si no con la clase
 
persona1.contador_persona=10
print(persona1.__dict__)         

# El atributo anterior oculta al atributo de clase
print(Persona.contador_persona) # Atributo de clase 
print(persona1.contador_persona) # Atributo del objeto


# Un segundo objeto

persona2=Persona("Mario","Kempes") 
print(persona2.__dict__)         
print(persona2.contador_persona)

# Asocuar un nuevo atributo de clase al vuelo(en el momento)
Persona.contador2=23
print(Persona.contador2)












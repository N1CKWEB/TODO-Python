# Funciones en python

def mi_primera_funcion_en_python(nombre,apellido):
    print("Saludos desde mi funcion")
    print(f"Nombre: {nombre} y su apellido es: {apellido}")
    
    
mi_primera_funcion_en_python("Juan","Luis") 
mi_primera_funcion_en_python("Karla","Lara")    
    
# Palabra return en funciones con python:

def suma(num1,num2):
    return num1 + num2

print(f"Resultado de la suma: {suma(22,1)}")



# Valores por default en los parámetros de una función:
def suma2(num1:int = 2, num2:int = 4) -> int:
    return num1 + num2

print(f"Resultado de la segunda suma: {suma2()}")
 
print("\n")

# Arguementos Variables en python

def listar_nombres(*nombres):
    for nombre in nombres:
        print(nombre)
        
        
listar_nombres("Nico","IA","Python","ML","DL","DataScience")

listar_nombres("NyckDev",23)


# Ejercicio 1 - Funciones

def sumar(*args):
    total = 0
    for arg in args:
       total += arg
    return total

resultado=sumar(1,2,3,4,5,6,7,2,5)
print(f"El resultado de la suma total es: {resultado}")

print("\n")

# Ejercicio 2 - Funciones

def multiplicar(*args):
    resultado = 4
    for numero in args:
        resultado *= numero
    return resultado

resultado2=multiplicar(3,4,6,7,8)
print(f"El resultado de la multiplicacion es: {resultado2}")

# Argumentos variables llave - valor en python:

def listarTerminos(nombre,*nombres,**terminos):
    for llave, valor in terminos.items():
        print(f"{llave}: {valor}")
        
     
        
# listarTerminos(IDE="Integrated Development Environment", ML="Machine Learning")


# Distintos tipos de datos como argumentos en python

def desplegar_nombres(nombre):
    for nombre1 in nombre:
        print(nombre1)
        
        
nombres=["Nico","Mari","Sergio","Juan"]

desplegar_nombres(nombres)        
desplegar_nombres("Mario")
desplegar_nombres([10,11])
desplegar_nombres((20,21))



# Funciones recursivas en python


def funciones_recursivas(numero):
    if numero == 1:
        return 1
    else:
        return numero * funciones_recursivas(numero-1)
    
print(f"El resultado de la recursivad: {funciones_recursivas(7)}")





# Ejercicio - Recursividad
def recursividad(numero):
     if numero >= 1:
       print(numero)
       recursividad(numero-1)
     elif numero == 0:
        return
     elif numero < 0:
        print("No recibe numeros negativos...")
        
        

recursividad(7)

# Ejercicio - Calculadora


pago_sin_impuesto=float(input("Proporcione el pago sin impuesto: "))
impuesto=float(input("Proporciones el monto del impuesto: "))

pago_total=pago_sin_impuesto+pago_sin_impuesto * (impuesto/100)

print(f"El pago total con impuesto es: {pago_total}")


# Ejercicio - Convertidor de Temperaturas

def celciusAFahrenheit(celcius):
    return (celcius * 9/5) + 32


def fahrenheitACelcius(falhrenheit):
    return   (falhrenheit-32) * 5/9 

print("\n")

celcius=float(input("Proporcione su valor en celcius: "))
resultado1=celciusAFahrenheit(celcius)

print("La conversión de celcius a fahrenheit es: ",resultado1)


falhrenheit=float(input("Proporcione su valor en falhrenheit: "))
resultado2=fahrenheitACelcius(falhrenheit)

print("La conversión de fahrenheit a celcius es: ",resultado2)
  
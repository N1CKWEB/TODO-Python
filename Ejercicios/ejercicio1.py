

import math 
import random
from random import choice 

# # Ejercicio - 1 - nivel fácil

# # def sumar():
# #     a=int(input('Introduce el primer numero: '))
# #     b=int(input('Introduce el segundo numero: '))
# #     resultado=a+b
# #     print(f"El resultado es: {resultado}")


# # sumar()


# # # Ejercicio - 2 - nivel fácil

# # def calcular_promerdio():
# #     num1=int(input('Introduce el primer numero:  '))
# #     num2=int(input('Introduce el segundo numero:  '))
# #     num3=int(input('Introduce el tercer numero:  '))
# #     resultado=num1+num2+num3
# #     total=resultado/3
# #     print(f"El promedio total es de: {total}") 
    
    
    
# # calcular_promerdio()



# # Ejercicio - 3 - nivel fácil

# def numero_positivo_negativo_o_cero(): 
#     a=int(input('Introduce el numero: '))
#     if a>1:
#         print('Positivo')
#     elif a<0:
#         print('Negativo')
#     elif a == 0:
#         print('Cero')    


# numero_positivo_negativo_o_cero()





# # Ejercicio - 4 - nivel fácil

# def area_de_un_circulo():
    
#     area=math.pi*math.pow(5,2)
#     print(f"El resultado del area de un circulo es: {area}")



# area_de_un_circulo()


# # Ejercicio - 1 - nivel intermedio


# def palabra_palindrome():
#     palindrome=input('Introduce una palabra palindrome: ').lower()
#     cadena_invertida = palindrome[::-1]
#     if palindrome == cadena_invertida:
#         print("Es palindrome")
#     else:
#         print('No es palindrome')
        
        
# palabra_palindrome()
        
        
# #Ejercicio - 2 - nivel intermedio

# def suma_de_numeros_en_un_rango():
#       num1=int(input('Introduce el primer numero: '))
#       num2=int(input('Introduce el segundo numero: '))
#       acumulador=0
#       for numeros in range(num1,num2+1):
#          acumulador=acumulador+numeros      
         
#       print(f"La suma total del rango es: {acumulador}")
    

# suma_de_numeros_en_un_rango()

    
# # Ejercicio - 3 - nivel intermedio
 
# def inversion_de_cadena(): 
#      cadenas=input('Escribe una cadena de texto: ')
#      nueva_cadena=""
#      for cadena in cadenas:
#         nueva_cadena=cadena+nueva_cadena
#      print(nueva_cadena) 
       
       
       
# inversion_de_cadena()       




# # Ejercicio - 4 - nivel intermedio



# def calculo_de_potencia():
#     numeros=int(input("Introduce el numero: "))
#     potencia=int(input("Introduce la potencia: "))
#     resultado=1
#     contador=0
#     while contador < potencia: 
#         contador=contador+1
#         resultado*=numeros
#     print(f"El resultado es: {resultado} y la cantidad de veces el contador: {contador}")   

# calculo_de_potencia()


# # Ordenamiento por Burbuja:

# # Implementa el algoritmo de ordenamiento por burbuja para una lista de números enteros.
# # Pista: Compara pares adyacentes y cámbialos si están en el orden incorrecto. Repite hasta que la lista esté ordenada.
# # Calculadora con Funciones:

def algoritmo_de_ordenamiento_de_burbuja():
     numeros=[1,23,8,2,6]
# Recorremos la lista hasta el penúltimo elemento
     for i in range(len(numeros) - 1):
      for j in range(len(numeros) - 1 - i):
         if numeros[j] > numeros[j + 1]:
           numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]   
      
      print(f"Lista nueva {i+1}: {numeros}")     
            

algoritmo_de_ordenamiento_de_burbuja()

# # Resumen:
# El -1 - i en el bucle interno asegura que:

# No te salgas de los límites de la lista (con el -1).
# Hagas menos comparaciones en cada iteración, ya que los elementos más grandes se van colocando al final de la lista en su lugar correcto (- i).



# # Crea una calculadora que realice operaciones básicas (suma, resta, multiplicación, división) usando funciones definidas por el usuario.
# # Pista: Define una función para cada operación y llama a la función adecuada según la elección del usuario.
# # Conteo de Palabras en un Archivo:
def sumar(num1,num2):
  return num1+num2

def resta(num1,num2):
 return num1-num2

def multiplicacion(num1,num2):
     return num1*num2

def division(num1,num2):
    return num1/num2

def calculadora():
   num1=float(input('Introduce el primer número: '))
   num2=float(input('Introduce el segundo número: '))
   operacion=input('Introduce la operación que quieres realizar: ')

   if operacion == "+" or  operacion == "suma":
        print(f"La suma total es: {sumar(num1,num2)}")
   
   elif operacion == "-" or  operacion == "resta":
        print(f"La resta total es: {resta(num1,num2)}")
   
   elif operacion == "*" or  operacion == "multiplicacion":
        print(f"La multiplicacion total es: {multiplicacion(num1,num2)}")
   
   elif operacion == "/" or  operacion == "division" and num2 !=0:
        print(f"La division total es: {division(num1,num2)}")
   
   else:
     return "No sé puede dividir por 0!"


calculadora()

# # Escribe un programa que lea un archivo de texto y cuente el número de palabras en él.
# # Pista: Usa la función open() para abrir el archivo y split() para dividir el texto en palabras.
# # Simulación de Juego de Dados:

try:
 with open('pythonIA.txt', encoding='UTF-8') as file:
  texto=file.read()
  palabras=texto.split()
  print(f"El contenido del archivo es: {texto}")
  print(f"El número total de palabra es: {len(palabras)}")
except Exception as e:
     print(f'El error es: {e}')
finally:
     file.close()
     ("Fin del archivo!")    
     
# # Crea un programa que simule el lanzamiento de dos dados y cuente cuántas veces se obtiene un par de números iguales en 100 lanzamientos.
# # Pista: Usa la función random.randint() para simular el lanzamiento de un dado.
# # Generador de Contraseñas:

def lanzamientos_de_dados():
  
     contador_pares=0
     contador_impares=0
     for dados in range(1,100):
       dado1=random.randint(1,6)
       dado2=random.randint(1,6)
       if dado1 == dado2:
          contador_pares=contador_pares+1
          print("Es par")
       else:
          contador_impares=contador_impares+1
          print("Es impar")           
     print(f"Registro de veces que fueron pares: {contador_pares}")     
     print(f"Registro de veces que fueron impares: {contador_impares}")     

lanzamientos_de_dados()

# # Escribe un programa que genere una contraseña aleatoria con una longitud específica y que contenga letras mayúsculas, minúsculas, números y símbolos.
# # Pista: Usa la biblioteca random y la función choice() para seleccionar caracteres aleatorios de diferentes conjuntos.


def generador_de_contraseña():
     
     mayusculas=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
     minisculas=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
     numeros=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22"]
     simbolos_especiales=["%","$","#","@","!","/","&"]
     
     
     
     contraseña_aleatoria=[]
     for i in range(12):
        # Escoge un tipo de carácter aleatorio y añade uno de ellos a la contraseña
        tipo = random.choice([mayusculas, minisculas, numeros, simbolos_especiales])
        contraseña_aleatoria.append(random.choice(tipo)) 
          
     contraseña_aleatoria_nueva="".join(contraseña_aleatoria)    
     print(f"La contraseña aleatoria es:{contraseña_aleatoria_nueva}")


generador_de_contraseña()








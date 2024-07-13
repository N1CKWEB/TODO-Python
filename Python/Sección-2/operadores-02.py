#Operadores en python


#Operador aritmetico "+"


operandoA=3
operandoB=2

suma=operandoA+operandoB

print(suma)

print(f'Resultado suma:{suma}')

#Operador aritmetico "-"


operandoC=2
operandoD=1

resta=operandoC-operandoD

print(resta)

print(f'Resultado resta:{resta}')


#Operador aritmetico "*"


operandoE=2
operandoF=1

multiplicacion=operandoE*operandoF

print(multiplicacion)

print(f'Resultado multiplicacion:{multiplicacion}')



#Operador aritmetico "/"


operandoG=2
operandoH=1

division=operandoG*operandoH

print(division)

print(f'Resultado division:{division}')

#Operador aritmetico "**"

operandoI=4
operandoJ=5

exponente=operandoI**operandoJ

print(exponente)

print(f'Resultado exponente{exponente}')

#Ejercicio-Rectángulo

alto=int(input("Introduce el alto: "))

ancho=int(input("Introduce el ancho: "))

area=alto*ancho

perimetro=(alto+ancho)*2

print(f"El area es: {area}")

print(f"El perimetro es: {perimetro}")


#Operadores de asignación

miVariable=23

print(miVariable)

#Operadores de Comparación

# a=4
# b=6
# resultado = (a == b)

# print(f"El resultado es: {resultado}")


# resultado=(a != b)

# print(f"El resultado es: {resultado}")


# Ejercicio - número par o impar

num=int(input("Introduce un número: "))

if num % 2 == 0:
  print("El número es par")
else:
  print("El número es impar")
  
#Ejercicio - mayor de edad

edad=int(input("Introduce una edad: "))

if edad >= 18:
    print("Es mayor de edad!")
else:
    print("Es menor de edad!")

#Operadores lógicos

# and , or o not

a = False 
b = False

if a or b:
    print("Es verdadero")
else:
    print("Es falso")

resultado = not a

print(resultado)

#Ejercicio- Valor dentro de rango


numRango=int(input("Proporciona el número: "))

if numRango>=0 and numRango<=5: 
    print("Esta en el rango!!!")
else:
    print("No esta en el rango!")
    
    
#Operador or
 
vacaciones=True

diaDeDescanso=False

if vacaciones or diaDeDescanso:
    print("Puede asistir al juego")
else:
    print("No puede asistir al juego")
    
    
#Operador not

if not (vacaciones or diaDeDescanso):
    
    print("No puede asistir al juego")
    
else:
    print("Puede asistir al juego")
    

#Ejercicio . Rango entre 20s y 30s

  
    
personaEdad=int(input("Introduce tu edad: ")) 

# veinte= 20 <= personaEdad < 30
# print(veinte)
# treinta= 30 <= personaEdad < 40
# print(treinta)


if (20 <= personaEdad < 30) or (30 <= personaEdad < 40):
  print("La persona es mayor y entra en el rango entre 20 y 30 años")
#   if veinte:
#       print("Dentro de los 20's")
# elif treinta:
#     print("Dentro de los 30's ")
else:
    print("La persona es mayor pero no entra en el rango entre los 20 y 30 años")



num1=int(input("Introduce el primer número: "))

num2=int(input("Introduce el segundo número: "))

if (num1>num2):
    print(f"El número mayor es el número 1 que es: {num1}")
elif (num2>num1):
    print(f"El número mayor es el número 2 que es: {num2}")
    
    
nombre=input("Introduce el nombre del libro: ")
id=int(input("Introduce el ID del libro: "))
precio=float(input("Introduce el precio del libro: "))
envio=bool(input("Indica si el envio es gratuito ( True / False): "))

print("\n")

print(f"El nombre del libro es: {nombre}")
print(f"El ID del libro es: {id}")
print(f"El precio del libro es: {precio}")
print(f"El envio del libro es: {envio}")

if envio == True:
    envio=True
elif envio == False:
    envio=False
else:
    print("Valor incorrecto, debe escribir True o False")
    
    
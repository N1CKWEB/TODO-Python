
# List Comprehensions en python


numeros=range(10)

lista_pares=[]

# Creamos una nueva lista, con los valores pares multiplicado por si mismo
for numero in numeros:
    # revisamos si es par o no
     if numero % 2 == 0:
         lista_pares.append(numero*numero)
       



print(f'Lista pares: {lista_pares}')
  



# Hacemos lo mismo pero con list comprehensions

# [expresion for var in coleccion if condicion]

# La condición del if es opcional
lista_pares=[]
lista_pares=[numero*numero for numero in numeros if numero % 2 == 0]
print(f"Lista pares con list comprehensions: {lista_pares}") 


# Un ejemplo similar con dos condiiciones (las condiciones recordemos son opcionales)
# solo se agrega el valor a la lista cuando el valor cumple ambas condiciones, es decir, debe ser divisible entre 2 y divisible entre 6.

pares=[numero for numero in range(50) if numero % 2 == 0 if numero % 6 == 0]


print(f"Lista divisible entre 2 y entre 6: {pares}")

# Agregamos if else
lista_pares=[]

lista_impares=[]

for numero in range(10):
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
        
print(f"Lista de pares: {lista_pares}")            
print(f"Lista de impares: {lista_impares}")            

# El mismo ejercicio, pero usando list comprehesions


lista_pares=[]
lista_impares=[]
[lista_pares.append(numero) if numero % 2 == 0 else lista_impares.append(numero) for numero in range(10)]


print(f"Lista de pares: {lista_pares}")            
print(f"Lista de impares: {lista_impares}")            



# Lista de listas

lista_de_listas=[[1,2,3],[4,5,6],[7,8,9,10]]

# Convertimos la lista de lista en una sola lista

lista_simple=[valor
              for sublistas in lista_de_listas 
              for valor in sublistas ]

print(f"Lista simple: {lista_simple}")


# Ahora creamos una lista de números de pares a partir de la lista_de_listas
# Sin list comprehensions,ciclos for anidados

lista_pares=[]
for sublista in lista_de_listas:
    for valor in sublista:
       if valor % 2 == 0:
          lista_pares.append(valor)
print(f"Lista pares sin usar list comprehensions: {lista_pares}")
          
#Con list comprehensions, en una sola linea de código, no es necesario separar las líneas, solo es para mejor lectura de código   
lista_pares=[]

lista_pares=[valor
             for sublista  in lista_de_listas 
             for valor in sublista 
             if valor % 2 == 0 ]

print(f"Lista pares usando list comprehensions: {lista_pares}")





















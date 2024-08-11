


# Profundizando en listas en python
# Listas son mutables, signifiica que se pueden modificar


nombres=['Nicolás','Juan','Naim','Gordo']
nombres2='Sergio Mariela Olga  Priscila Lautaro'.split()

# Sumar una lista
 
print(f"Suma de lista {nombres+nombres2}")

# Extender una lista con otra lista

nombres.extend(nombres2)
print(f"Extender la lista: {nombres}")



# Profundizando en listas - segunda parte


numeros1=[10,40,15,4,80,23]
print(f"Lista original: {numeros1}")
# Obtener el indice del primer elemento encontrado en una lista


# help(list.index)



print(f"Indice 4: {numeros1.index(4)}")



# Invertir el orden de los elementos de una lista

numeros1.reverse()

print(f"Lista invertida: {numeros1}")


# Ordena los elementos de una lista ASC
numeros1.sort()
print(f"Lista ordenada ascendente: {numeros1}")

# Ordena los elementos de una lista DESC
numeros1.sort(reverse=True)

print(f"Lista ordenada descendente: {numeros1}")



# Copiando listas 

# Obtener valor minimo y maximo de una lista


# Valor Minimo 

print(f"Valor minimo: {min(numeros1)}")

# Valor Máximo

print(f"Valor maximo: {max(numeros1)}")

# Copiar elementos de una lista

# shallow - Poco profunda
# help(list.copy)


numeros2=numeros1.copy()

print(f"Lista 2: {numeros2}")

# Con (is) preguntamos si es la misma referencia en memoria
print(f"Misma referencia? {numeros1 is numeros2}")

# Con (==) preguntamos si es el mismo contenido

print(f"Mismo contenido? {numeros1 == numeros2}")



# Podemos usar el constructor de la lista

numeros2=list(numeros1)

print(f"Misma referencia? {numeros1 is numeros2}")

print(f"Mismo contenido? {numeros1 == numeros2}")


# slicing 

numeros2=numeros1[:]


print(f"Misma referencia? {numeros1 is numeros2}")

print(f"Mismo contenido? {numeros1 == numeros2}")

# Lista de listas


# Multiplicación de listas

lista_multiplicacion=5*[[2,5]]

print(lista_multiplicacion)


print(f"Misma referencia? {lista_multiplicacion[0] is lista_multiplicacion[1]} ")

print(f"Mismo contenido? {lista_multiplicacion[0] == lista_multiplicacion[1]} ")

lista_multiplicacion[2].append(10)

print(f"Lista modificada {lista_multiplicacion}")



# Matrices en python

matriz=[[10,20],[30,40,50],[60,70,80]]

print(f"La matriz original: {matriz}")

print(f'Renglon 0, columna 0: {matriz[0][0]}')
print(f'Renglon 2, columna 1: {matriz[2][1]}')



matriz[2][1]=75

print(f"Matriz modificada: {matriz}")


# Ordenamiento de Listas

lista_listas=[ [90,105,275,365,1022,101],[23,26,64,3,4,385],[0,4,7,2],[11,56,10,14,17,21]]

lista_listas.sort(key=len)
print(f"Lista original: {lista_listas}")



# sorted built-in

# help(sorted)

nombres1=['Juan Carlos','Karla','Pedro','Esperanza']

nombres1=sorted(nombres1)

print(nombres1)

# Ordena de manera descendente
nombres1=sorted(nombres1, reverse=True)

print(nombres1)


# Ordenar por la cantidad de los caracteres (largo)

nombres1=sorted(nombres1, key=len)

print(nombres1)



# built-in reversed
nombres1=reversed(nombres1)

print(list(nombres1))






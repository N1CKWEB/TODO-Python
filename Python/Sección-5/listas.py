#Primera vez que usamos listas, definir una lista de tipo str, son entre corchetes las listas 

nombres = ["Juan","Karla","Nico","Mariela","Sergio"]

#imprimir las lista de nombres 
print(nombres)

#Acceder a los elementos de una lista, de manera inversa

print(nombres[-1])
print(nombres[2])

# Acceder a un rango

print(nombres[0:3])

#Ir del inicio de la lista al índice (sin incluirlo)

print(nombres[:7])

#Desde el indice indicado hasta el final

print(nombres[1:]) 
print(nombres[2:]) 

# Cambiar el valor

nombres[3] = "Mario" 

print(nombres)

#Iterar una lista

for nombre in nombres:
    print("Los nombres son: ", nombre)
else:
    print("No existen mas nombres en la listas")
    
    
# Preguntar el largo de una lista
print(len(nombres))  #len: te da la cantidad total 

# Agregar un elemento:

nombres.append("lorenzo") #append:agrega un elemento 
print(nombres)

# Insertar un elemento en un indice en especifico

nombres.insert(1,"Octavio")

print(nombres)

# Remover un elemento

nombres.remove("Octavio")

print(nombres)

# Remover el último valor agregado

nombres.pop()

print(nombres)

# Eliminar un indice

del nombres[0]
print(nombres)

# Limpiar la lista

nombres.clear()
print(nombres)

# Elimina la lista por completo

# del nombres
# print(nombres)


# Ejercicio 1 - Iterar un rango de 0 a 10 e imprimir números divisibles entre 3.

print("Numeros con un rango entre 0 a 10, y divisibles entre 3")
for i in range(11):
 if i % 3 == 0:
   print(i) 

#Ejercicio 2 - Crear un rango de números de 2 a 6, e imprimelos.

print("Numeros con un rango entre 2 a 6")
rango=range(2,7)
for i in rango:
    print(i)

#Ejercicio 3 - Crear un rango de 3 a 10, pero con incremento de 2 en 2, en lugar de 1 en 1

print("Numeros con un rango entre 3 a 10")
rango=range(3,11,2)
for i in rango:
    print(i)
    
    
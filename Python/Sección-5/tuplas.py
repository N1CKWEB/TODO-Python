# Tuplas en python, las tuplas son con parentesis, las tuplas también no se pueden cambiar al menos que la hagas listas

# Definir una tupla:

frutas=("Naranja","Platano","Guayaba")


# Saber el largo de la tupla

print(len(frutas))

# Acceder a un elemento

print(frutas[0] )

# Navegación inversa

print(frutas[-2])


# Acceder a un rango

print(frutas[1:2])  #Sin incluir el último indice 

print("\n")

#Recorrer elementos
print("Recorriendo una tupla: ")
for fruta in frutas:
    print(fruta, end=' ')
    
    

#Cambiar el valor de la tupla:

# frutas[0]="Pera"

frutaLista=list(frutas)

frutaLista[0]="Pera"

frutas=tuple(frutaLista)

print("\n", frutas)


# Eliminar la tupla por completo

# del frutas
# print(frutas)


# EJercico - crear una lista que solo incluya los números menores a 5

tupla=(13,1,8,3,2,5,8)
lista=[]

for i in tupla:
    if i < 5:
        lista.append(i)

#Imprimimos la lista 
print(lista)
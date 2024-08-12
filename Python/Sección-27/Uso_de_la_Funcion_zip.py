

# Uso de la función zip en python


# La funcion zip nos va a permiter unir uno o más iterables,lo que hace es que vamos a poder unir listas, tuplas, cualquier iterable los podemos unir

# Zip significa comprimir



# print(dir(__builtins__))

# Combinando una tupla con una lista y un nombres

numeros=(1,2,3)
letras=['A','B','C']
# nombres={'Nombre':'Nicolás','Edad':19}
identificadores=19,20,21,22,23
conjuntos={1,2,3,4,5,6}
mezlas=zip(numeros,letras,identificadores,conjuntos)
# print(type(mezlas))
print(f"La union es: {list(mezlas)}")
# print(set(zip(numeros,letras,nombres)))

# Iterar en paralelo

# for numero,letra,identificadores,aleatorio in zip(numeros,letras,identificadores,conjuntos):
#     print(f"Numeros: {numeros}, letras: {letras} , id:{identificadores} , Aleatorio: {aleatorio}")


nueva_lista=[]
for numero,letra,identificadores,aleatorio in zip(numeros,letras,identificadores,conjuntos):
      nueva_lista.append(f'{identificadores}-{numero}-{letra}-{aleatorio}')

print(nueva_lista)



# Proceso unzip, separando los elementos de cada lista,tuplas,diccionarios o sets

mezcla=[(1,'a'),(2,'b'),(3,'c')]

numeros,letras=zip(*mezcla)

print(f"Numeros: {numeros}, Letras: {letras}")


# Ordenar un zip, ordenamiento usando zip

letras=['c','d','a','e','b']
numeros=[4,5,6,23,0,1]


mezclas=zip(letras,numeros)

print(f"Zip desordenado: {tuple(mezclas)}")

# Ordenar zip

print(f"Zip ordenado: {sorted(zip(numeros,letras))}")

# Crear un diccionario con zip

llaves=['Nombres','Edad','Provincia']
valores=['Nicolas',19,'Mendoza']


mezcla_diccionario=dict(zip(llaves,valores))

print(f"Mezcla de diccionarios: {mezcla_diccionario}")


# Actualizar un elemento de nuestro diciconario

llaves=['Edad']
nueva_edad=[19]

# Con en el metodo update usado para diccionarios, se puede actualizar un nuevo elemento de la llave o de valores, y también se puede usar para agregar una llave o valor
mezcla_diccionario.update(zip(llaves,nueva_edad))

print(mezcla_diccionario)







 
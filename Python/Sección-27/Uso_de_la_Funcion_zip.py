

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



# Proceso unzip 





 
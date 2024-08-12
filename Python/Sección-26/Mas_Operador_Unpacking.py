

# Más de Operador Unpacking en Python
# Nos sirve para desempaquetar


numeros=[2,3,4]

print(f"Lista original: {numeros}")


print(*numeros)

print(*numeros,sep='-')


# Desempaquetando al momento de pasar un parametro a una función
def sumar(a,b,c):
    print(f"El resultado de la suma {a+b+c}")


# Lo que hago es desempaquetar la lista con el operador unpacking
sumar(*numeros)



# Desempaquetado con variables, extraer algunos partes de una lista

mi_lista=[1,2,3,4,5,6]

a,*b,c,d=mi_lista

print(a,b,c,d)



# Crear listas con el operador Unpacking


# Unir listas

listas1=[1,2,3]
listas2=[4,5,6]

listas3=[listas1,listas2]

print(f"Lista de listas: {listas3}")

lista=[*listas1,*listas2]

print(f"Unir listas: {lista}")


diccionario1={'A':1,'B':2,'C':3}
diccionario2={'D':4,'E':5,'F':6}

new_diccionario = {**diccionario1 , **diccionario2}

print(f"Nuevo diccionario: {new_diccionario}")




# Construir una lista a partir de un str

lista=[*'HolaMundo']
print(*lista,sep='')


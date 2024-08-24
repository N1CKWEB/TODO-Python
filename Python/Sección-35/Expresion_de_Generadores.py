


# Expresión generadora (Es un generador anónima)



multiplicacion = (valor*valor for valor in range(4))

print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))


# También se puede pasara una expresión generadora a una función(sin usar parentesis)

import math 
suma=sum(valor*valor for valor in range(4))

print(f"El resultado de la suma es: {suma}")





# También podemos usar una lista o cualquier otro iterador

lista=['Juan','Perez']

generador=(valor for valor in lista)
print(next(generador))
print(next(generador))

# Crear un string a partir de un generador a partir de una lista

lista=['Nico','Diaz',19]

contador=0

# Definimos una función para incrementar el contador
def incrementar():
 global contador
 contador+=1
 return contador

#La primera para es el yield, la segunda parte es el for, entre parentesis

generador=(f'{incrementar()} . {nombre}' for nombre in lista)
lista=list(generador)
print(lista)

cadena=' , '.join(lista)

print(f'Cadena generada: {cadena} ')

























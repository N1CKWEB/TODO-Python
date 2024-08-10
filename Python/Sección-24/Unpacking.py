

# Unpacking (Desempaquetando) en python

valores=1,2,3

print(type(valores))


valor1,_,valor3=1,2,3
print(valor1,valor3)


valor1,valor2,*valor3 = 1,2,3,4,5,6,7,8,9
print(valor1,valor2,valor3)

valor1,valor2,*valor3,valor4,valor5 = 1,2,3,4,5,6,7,8,9
print(valor1,valor2,valor3,valor4,valor5)

# Unpacking segunda parte

valor1,valor2,*valor3,valor4,valor5 = [1,2,3,4,5,6,7,8,9]
print(valor1,valor2,valor3,valor4,valor5)



def regresa_varios_datos():
    return 1,2,3



valor1,valor2,valor3=regresa_varios_datos()

print(valor1,valor2,valor3)

valor1,*_valores_restantes=regresa_varios_datos()

print(valor1,_valores_restantes)

# Ejemplo de Unpacking

# help(str.partition)



hora,_,minutos='17:20'.partition(':')

print(hora, minutos)



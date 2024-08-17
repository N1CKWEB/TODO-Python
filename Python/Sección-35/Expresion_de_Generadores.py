


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




























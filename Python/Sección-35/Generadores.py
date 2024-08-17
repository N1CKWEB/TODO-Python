


# Generadores en python, es una función especial en python el cual nos permite devolver una sequencia de valores, pero esta secuencia de valores no se devuelven todos los valores al mismo tiempo, la palabra reservada yield="producir" para devolver todos los valores, supende la ejecución de la función por medio de la función "yield" y no se usa "return"

def generador():
    yield 1
    print('Se reanuda la ejecucion')
    yield 2
    print('Se reanuda la ejecucion')
    yield 3
    

# Cosumir el generador a demanda
gen=generador()

#Con cada llamada consumimos un valor
print(next(gen)) 
print(next(gen)) 
print(next(gen)) 

# Si tratamos de consumir más valores de los que produce el generador, lanza un error de StopIteration.
# print(next(gen)) 


# Consumiendo los valores del generador con un ciclo "for"
for valor in generador():
   print(f"Numero generado {valor}")   























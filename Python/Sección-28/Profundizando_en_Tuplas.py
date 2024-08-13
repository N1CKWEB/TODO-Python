
# Profundizando en tuplas en python

# Podemos usar tuplas para declarar variables



a,b='Hola','Adios'

print(a,b)

# swap(intercambio de variable)

a,b=b,a

print(a,b)

# Regresar múltiples valores en una función

def minmax(elementos):
    return min(elementos),max(elementos)


min,max=minmax([1,2,3,4,5])

print(f"Valor min: {min}, Valor max: {max}")



# Regresar la suma de una tupla

res=sum((1,2,3,4,5))

print(f"El resultado final es: {res}")

def suma(*args):
    return sum(args)


suma=suma(1,2,3,4,5)

print(f"La suma final es: {suma}")




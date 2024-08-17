



# Decoradores 
# Un decorador es una función que recibe a sus vez una función y regresa otra, y lo utilizamos para extender funcionalidad
# 1. Función decorador (a)
# 2. Función a decorar (b)
# 3. Función decorada  (c)

# Aplicando decoradores y closures para mejorar la forma de hacer funciones
def funcion_decorador_a(funcion_a_decorar_b):
    
    def funcion_decorada_c(*args, **kwargs):
        print('Antes de ejecutar la funcion_decorada_c')
        resultado=funcion_a_decorar_b(*args, **kwargs)
        print('Despues de ejecutar la  funcion_decorada_c')
        return resultado
    
    
    return funcion_decorada_c


@funcion_decorador_a
def sumar(a,b):
    return a+b
def restar(a,b):
    return a-b
def multiplicar(a,b):
    return a*b
def dividir(a,b):
    return a/b

resultado=sumar(22,1)

print(f"El resultado de la suma es: {resultado}")

resultado=restar(22,1)
print(f"El resultado de la resta es: {resultado}")

resultado=multiplicar(22,1)
print(f"El resultado de la multiplicacion es: {resultado}")


resultado=dividir(22,1)
print(f"El resultado de la division es: {resultado}")
















































# Funciones y sus distintos uso, las funciones en python son ciudadanas de primera clase, First Class Citizens



# Definimos la función 
def sumar(a,b):
    return a+b



# 1. Asignar una función a una variable (no se usa parentesis)

mi_funcion=sumar


# Verificar el tipo de variable

print(type(mi_funcion))


# Llamamos la función a través de la variable
resultado=mi_funcion(2,3)

print(resultado)


# 2. Función como argumento

def operacion(a,b,sumar_arg):
    print(f'Resultado de sumar: {sumar_arg(a,b)}')


operacion(22,1,sumar)

# 3. Podemos retornar una función desde otras funciones

def retornar_funcion():
 # Retornamos una función
  return sumar



mi_funcion_retornada=retornar_funcion()

print(f"Resultado de la funcion retornada {mi_funcion_retornada(2,3)}")




















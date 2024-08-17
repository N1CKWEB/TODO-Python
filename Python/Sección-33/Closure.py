


# Funciones closures en python, mantiene un estado, un closure es una función que defina a otra, y ademas la puede regresar, la función anidada puede acceder a las variables locales definidas en la función principal o externa.




# Función principal

# def operacion(a,b):
#     # Definimos una función interna o anidada
#     def sumar():
#       return a+b

#     # Retornar la función
#     return sumar

# Función principal
def operacion(a,b):
    # 1. Definimos una función lambda interna o anidada y la retornamos 
    return lambda:a+b


mi_funcion=operacion(3,3)

print(f"Resultado: {mi_funcion()}")


# Llamar la función regresada al vuelo

print(f"Resultado de la funcion closure al vuelo: {operacion(1,1)()}")



























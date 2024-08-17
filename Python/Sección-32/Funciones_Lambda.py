



# Funciones Lambdas en python, son funciones anonimas y pequeñas (Una línea de código son)

# No es posible una función a una variable
#mi_funcion= def sumar(a,b): return a+b



# Concepto de una función lambda (anónima, sin nombre, y una sola línea de código ), no sé necesita agregar paréntesis para los parámetros y la palabra return no se necesita utilizar, pero si debe regresar una expresión valida


mi_funcion_lambda=lambda a,b : a+b

print(f"Resultado final con funcion lambda: {mi_funcion_lambda(2,2)}")



# Funciones lambda - segunda parte


# Funcion lambda que no recibe argumentos


mi_funcion_lambda_2=lambda: 'Funcion sin argumento'


print(f"Llamar funcion lambda sin argumentos: {mi_funcion_lambda_2()}")


# Función lamda con parametros por default

mi_funcion_lambda=lambda a=22,b=1 : a+b 

print(f"Resultado de argumentos por default con lamda: {mi_funcion_lambda()}")


# Función lambda con argumentos variables: *args **kwargs

mi_funcion_lambda=lambda *args, **kwargs : len(args) + len(kwargs)

print(f"Resultado de argumentos variables de lambda:   {mi_funcion_lambda(1,2,3,a=3,b=2,c=2)}")



# Funciones lambda con argumentos, argumentos variables y valores por default

mi_funcion_lambda=lambda a,b,c,*args, **kwargs : a+b+c+len(args)+len(kwargs)

print(f"Resultado de la funcion lamda: {mi_funcion_lambda(1,2,3,4,5,6,7,e=5,f=22)}")























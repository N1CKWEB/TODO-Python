


# Funciones anidadas en python


def calculadora(a,b,operacion='sumar'):
    # Función anidada
    def sumar(a,b):
             return a+b
    def restar(a,b):
             return a-b 
  #Llamamos a la función anidada 
    if operacion=='sumar':
       print(f"Resultado final de suma: {sumar(a,b)} ")
    elif operacion=='restar':
       print(f"Resultado final de restar: {restar(a,b)} ")



calculadora(22,1,operacion='Sumar')
calculadora(22,1,operacion='restar')




























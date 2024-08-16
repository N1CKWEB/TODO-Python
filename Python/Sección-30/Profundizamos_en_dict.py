


# Los diccionarios guardan un orden (a diferencia de un set)

diccionario={"Nombre":"Nicolas","edad":19,"Pais":"Mendoza"}

print(diccionario)



# Los diccionarios son mutables,pero las llaves deven ser inmutables
# diccionario={[1,2]:'valor1'}
# diccionario={(1,2):'Valor1'}
# print(diccionario)


# Se agrega una llave con su valor, si no se encuentra dentro del diccionario

diccionario['Provincia']='Mendoza'

print(diccionario)


# No hay valores duplicados en las llaves de un diccionario(si ya existe se reemplaza)

diccionario['Nombre']='Sergio'

print(diccionario)


# Recuperar un valor indicando una llave

print(diccionario['Nombre'])

# Si no encuentra la llave, lanza una excepción
# print(diccionario['nombre'])

# Método (get) recupera una llave, y si no existe NO lanza una excepcion, admeas podemos regresar un valor en caso de que no exista la llave

print(diccionario.get('Nombree','No se encontro la llave'))


# Método (setdefault) si modifica el diccionario, en caso de que no encuentre la llave, ademas se agrega un valor por default

print(diccionario.setdefault('Nombres','Valor por default'))
print(diccionario)


# Forma más simple de imprimir un diccionario, con (pprint)

from pprint import pprint

help(pprint)

pprint(diccionario,sort_dicts=False)



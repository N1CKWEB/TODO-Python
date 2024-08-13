

# Profundizando en Set con python

# Un set es una colección de elementos únicos y es mutable

# Los elementos de un set debe ser inmutables

conjunto = {'Juan',False,1.2}
print(conjunto)


# Generar un diccionario vacio
conjunto={}
print(type(conjunto))


# Un set vacio definir de manera correcta

conjunto=set()

print(conjunto)
print(type(conjunto))


# Mutable

conjunto.add('Nico')

print(conjunto)

# Contiene valores unicos

conjunto.add('Nico')

print(conjunto)

# Crear un set a partir de un iteravble

conjunto=set([4,5,6,7,8,4])

print(conjunto)


# Podemos agregar más elementos o incluso otro set

conjunto2={100,200,300,300}

conjunto.update(conjunto2)

print(conjunto)

conjunto.update([20,30,40,40])

print(id(conjunto))


# Copiar un set a otro set, poco profunda la copia, solo copia referencia

conjunto_copia=conjunto.copy()

print(f"La copia de conjunto {id(conjunto_copia)}")

# Verificar la igualdad de estos dos set

print(f"Tienen la misma referencia? {conjunto is conjunto_copia}")
print(f"Tiene en el mismo contenido? {conjunto == conjunto_copia}")


# Operaciones Algebraicas con Set con conjuntos 

# Personas con distintas caracteristicas

personas_pelo_negro={'Mia','Mariela','Sergio','Prisci'}

personas_pelo_rubio={'Isa','Juan','Mirko','Martin'}

ojos_verdes={'Mia','Prisci','Juan'}

menores_de_30={'Prisci','Juan','Nico','Mirko'}

# Todos los elementos con ojos verdes y pelo rubio(Union) (No se repiten los elementos en un set)

# Función de Union:
print(ojos_verdes.union(personas_pelo_rubio))
# Invertir el orden con el mismo resultado (conmutativo)
print(personas_pelo_rubio.union(ojos_verdes))


# Función de Intersección, operacion(intersection): Solo las personas con ojos verde y pelo rubio

print(ojos_verdes.intersection(personas_pelo_rubio))

# Invertir el orden con el mismo resultado (conmutativo)
print(personas_pelo_rubio.intersection(ojos_verdes))

 

# Función de diferencia, operación(difference), está función no es conmutativa: Solo las personas con  pelo negro pero sin ojo verdes

# Las personas que se encuentra en el primer set, pero no en el segundo
print(personas_pelo_negro.difference(ojos_verdes))

# Función (Symmetric Difference):
# Personas con pelo negro u ojos ojoes verdes pero no ambos
print(personas_pelo_negro.symmetric_difference(ojos_verdes))




# Funciones para preguntas con Set:
 
# subset,superset,disjoint

# Preguntas si un set esta contenido en otro (subset) 
# Revisamos si los elementos del primer set estan contenidos en el segundo set.

print(menores_de_30.issubset(personas_pelo_negro))



# Preguntar si un set contiene a otro set (superset)
# Revisar si los elementos del primer set estan contenidos en el segundo set

print(menores_de_30.issuperset(personas_pelo_negro))



# Preguntar si los de pelo negro no tiene pelo rubio (distjoint)

print(personas_pelo_negro.isdisjoint(personas_pelo_rubio))




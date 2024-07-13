# Los set en python, no matiene un orden, no permite duplicar elementos, los sets usan llaves
# Los set sirven para usarlo cuando no queremos que alla un elemento repetido


planetas={"Marte","Jupyter","Saturno"}
print(planetas)

# Largo de los elementos
print(len(planetas))

# Revisar si un elementos esta presente

print("Martes" in planetas)

# Agregar un elemento

planetas.add("Tierra")

print(planetas)

# No soporta elementos duplicados

planetas.add("Tierra")
print(planetas)

# Eliminar elementos posiblemente arrojando un error

planetas.remove("Tierra")

print(planetas)

# Eliminar un elemento sin arrojar error
planetas.discard("Jupyter")
print(planetas)

# Limpiar un elemento en set
planetas.clear()
print(planetas)

# Eliminar por completo el set
del planetas
print(planetas)
# Diccionarios en python, dict(keyword arguments)

diccionario={
    "IDE":"Integrated Development Enviroment",
    "OOP":"Object Oriented Programming",
    "DBMS":"Database Management System"
}
print(diccionario)

# Largo de nuestro diccionario
print(len(diccionario))

# Acceso a un elemento (key)
print(diccionario["IDE"])

# Otra forma de recuperar otro elemento
print(diccionario.get("OOP"))

# Modificando elementos:
diccionario["IDE"] = "integrated development enviroment "
print(diccionario)


# 2 - Parte de Diccionarios

# Recorrer los elementos de un diccionario 

# Con items podemos recorrer los terminos y valor
for terminos, valor in diccionario.items():
    print(terminos,": ",valor)
    
# Con keys podemos recorrer los terminos
for termino in diccionario.keys():
    print(termino)
    
# Con values podemos recorrer los valor 
for valor in diccionario.values():
    print(valor)    
    

# Comprobar existencia de algún elemento
print("IDE" in diccionario)


# Agregar un elemento a nuestro diccionario 

diccionario["PK"] = "Primary Key"

print(diccionario)

diccionario["ML"] = "Machine Learning"

print(diccionario)

# Remover un elemento

diccionario.pop("DBMS")

print(diccionario)

# Limpiar el diccionario

diccionario.clear()
print(diccionario)

# Eliminar todo el diccionario

del diccionario
print(diccionario)



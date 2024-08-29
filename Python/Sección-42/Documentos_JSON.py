
import urllib.request
import json


# Procesar Documentos JSON en Python


# API -Aplication Program Interface

# Leer archivo json

respuesta=urllib.request.urlopen('https://jsonplaceholder.typicode.com/users')

print(respuesta)

cuerpo_de_respuesta=respuesta.read()
print(cuerpo_de_respuesta)


print("\n")
# Procesamos la respuesta

json_respuesta=json.loads(cuerpo_de_respuesta.decode('UTF-8'))


print(f"Respuesta JSON correcta: {json_respuesta}")


# Imprimir sólo los nombres de las personas

# JSON se convierte a listas y diccionarios en python


for persona in json_respuesta:
    print(f"Persona: {persona['id']} {persona['name']} {persona['phone']}")
    

# Accedemos a las variables independientes

contador=0

for personas_json in json_respuesta:
    contador+=1  
    
print(f"Total de personas en el json: {contador}")
    
    
       













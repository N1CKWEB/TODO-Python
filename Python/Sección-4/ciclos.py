# condicion = True

# while condicion:
#   print("Verdadero!!")
# else:
#     print("Falso")



contador=0
 
while contador < 3 :
   print(contador)
   contador += 1 #contador = contador + 1
else:
   print("Fin ciclo while")     


# # # Ejercicio - Imprimir número del 0 al 5

maximo = 5 
contador = 0

while contador <= maximo:
    print(contador)
    contador += 1


# # Ejercicio 

minimo=1
contador=5

while  contador >= minimo:
  print(contador)
  contador -=1


# Ciclo For:

cadena="Hola"

for letra in cadena:
    print(letra)
else:
    print("Fin ciclo for!")    
    
    
# break en python: 
 
for letra in "Holanda":
    if letra == "a":
        print(f"Letra encontrada {letra}")
        break  #Lo que hace que detiene con todo lo que le sigue 
    else:
        print("!Fin ciclo for!")    
        
        
#Continue en python: 

# for i in range(6):
#     if i % 2 == 0:
#      print(f"Valor: {i}")
    
for i in range(6):
    if i % 2 != 0:
        continue   #continue ejecuta la siguiente iteracción y ya no ejecuta ninguna de la siguiente iterración
    print(f"Valor: {i}")
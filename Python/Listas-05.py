#Listas en python
#Recordatorio siempre las listas se usan con " [] "


my_list=list()

my_other_list=[]

print(len(my_list))

my_list=[34,14,47,13,60,45]

print(my_list)

print(len (my_list))

my_other_list=[19,1.83,"Nico","Diaz"]

print((my_other_list[0]))
print((my_other_list[-1]))
print((my_other_list[1]))
print((my_other_list[3]))

age,height,name,surname=my_other_list

print(name)

print(my_list+my_other_list) #Concatenación de dos listas

 
print(my_other_list.pop()) #Elimina el último elemento de la lista

print(my_list+my_other_list) #Concatenación de dos listas


#Trabajar con elementos de la listas:

my_other_list.append("Neon-i") #Lo inserta al final al elemento

my_other_list.insert(1,"Messi") #Inserta un objeto donde la posicion que le coloques

my_other_list.remove("Messi") #Elimina lo que le digas de el elemento de la lista

 

print(my_other_list)


print(my_list)


del my_list[2] #Con del podemos eliminar también una posición de la lista

print(my_list)

my_new_list=my_list.copy()

my_list.clear() #Lo que hace limpia toda la lista completa

print(my_list)

my_new_list.reverse() #Lo que hace reversa toda la lista
print(my_new_list)

my_new_list.sort() #Ordena la lista

print(my_new_list)
#Colas en python

print(my_new_list[1:2])

print(my_new_list)
 
 
 
 
 
 
 
 
 
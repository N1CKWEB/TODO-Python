#Acá veremos los strings y sus metodos

my_string="Mi String"
my_other_string="My otro string"

print(len(my_string))
print(len(my_other_string))


print(my_string+" "+my_other_string)

my_new_line_string="Este es un string \n con salto de linea"  #Salto de linea 

print(my_new_line_string)

my_tab_string="Este es un string con \t tabulacion" #Tabulación

print(my_tab_string)



#Formateo 

#Se usan llaves o el porcentaje con s, se usan llaves si tal cual quieres que imprima el objeto, usamos los %s o $d o $f si estamos trabajando con el número formateado.

name,lastname,age="Nicolas","Diaz",19

print("Mi nombre {} {} y mi apellido es {}".format(name,lastname,age))

print("Mi nombre %s %s y mi apellido es  %s" %(name,lastname,age))

#Inferencia de datos:

print(f"Mi nombre es {name} {lastname} y mi edad es: {age}")


#Desempaquetado de caracteres
lenguaje="Python"

a,b,c,d,e,f=lenguaje

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#Division

languaje_slice=lenguaje[1:3]

print(languaje_slice)

languaje_slice_s=lenguaje[0:6:2]
print(languaje_slice_s)

#Reverse

reversed_languaje=lenguaje[::-1]
print(reversed_languaje)


# Funciones y métodos de python

print(lenguaje.upper()) #Pone todo el texto en MAY
print(lenguaje.lower()) #Pone todo el texto en MIN
print(lenguaje.count("t")) #Cuenta la cantidad de letras que le pongas vos
print(lenguaje.capitalize()) #Pone la primera letra en MAY
print("1".isnumeric())  #Verifica si es un número o no
print(lenguaje.upper().isupper()) #Verifica si esta en MAY o no
print(lenguaje.lower().islower()) #Verifica si esta en MIN o no
print(lenguaje.startswith("Pyth")) #Comprueba si empieza con esas letras o no



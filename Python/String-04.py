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

name,lastname,age="Nicolas","Diaz",19

print("Mi nombre {} {} y mi apellido es {}".format(name,lastname,age))

print("Mi nombre %s %s y mi apellido es  %s" %(name,lastname,age))

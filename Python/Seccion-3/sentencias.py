# condicion=True


# if condicion:

#     print("Condición verdadera")

# elif condicion == False:

#     print("Condición Falsa")

# else:

#     print("Condición no reconocida")
    
    
# #Ejercicio - Conversión de Número a Texto

# numero = int(input("Proporciona un valor entre 1 y 3: "))
# numeroTexto = " "

# if numero == 1:
#    numeroTexto="Número uno"
# elif numero == 2:
#     numeroTexto="Número dos"
# elif numero == 3:
#     numeroTexto="Número tres" 
# else:
#     numeroTexto="Valor fuera de rango" 
              
              
# print(f"Número proporcionado: {numero} - {numeroTexto}")              
    
    
# condicion = True 

# # if condicion:
# #     print("Condición verdadera")
# # else:
# #     print("Condición Falsa")
    
    
# print("Condición verdadera") if condicion else print("Condición falsa")    
       
    


# # Ejercicio - Calcular la Estación según el Mes proporcionado

# mes = int(input("Proporciona mes del año: (1-12): "))

# estacion = None 

# if mes == 1 or mes == 2 or mes == 12:
#     estacion = "Invierno"
# elif mes == 3 or mes == 4 or mes == 5:
#     estacion = "Primavera"
# elif mes == 6 or mes == 7 or mes == 8:
#     estacion = "Verano"
# elif mes == 9 or mes == 10 or mes == 11:
#     estacion = "Otoño"
# else:
#     estacion = "Mes incorrecto"

# print(f"Para el mes {mes} la estación es: {estacion}")


# # Ejercicio - Etapas de vida según Edad


# edad=int(input("Proporciona tu edad: "))

# mensaje=None

# if  0 <= edad < 10:
#   mensaje="0-10: La infancia es increíble..."
#   print(f"Tu edad es: {edad} , {mensaje}")
# elif 10 <= edad < 20:
#     mensaje="Muchos cambios y mucho estudio..."
#     print(f"Tu edad es: {edad} , {mensaje}")
# elif 20 <= edad < 30:
#     mensaje="Amor y comienza el trabajo..."
#     print(f"Tu edad es: {edad} , {mensaje}")
# else:
#     print("Etapa de vida no reconocida")
#     print(f"Tu edad es: {edad} , {mensaje}")
    
    
# # Ejercicio - Sistema de Calificaciones


calificacion=int(input("Proporciona un valor entre 0 y 10: "))

nota=None

if  9 <= calificacion  <= 10:
    print("Una A")
elif 8 <= calificacion < 9:
    print("Una B")
elif 7 <= calificacion < 8:
    print("Una C")
elif 6 <= calificacion < 7:
    print("Una D")
elif 0 <= calificacion < 6:
    print("Una F")
else: 
    print("Valor incorrecto!!")
    
    
    

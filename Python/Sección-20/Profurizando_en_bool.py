

# Profundizando en el tipo bool en python


# Tipos numericos, False para el valor de 0 y True para los demas valores

valor=0.0
res=bool(valor)
print(f"Valor: {valor} , El resultado es: {res}")

valor=23.0
res=bool(valor)
print(f"Valor: {valor} , El resultado es: {res}")



# Tipo str, False para cuando usamos cadenas vacias '',  True para los demas valores



valor=""
res=bool(valor)
print(f"Valor: {valor} , El resultado es: {res}")

valor="Nicolas"
res=bool(valor)
print(f"Valor: {valor} , El resultado es: {res}")


# Tipos colecciones, False para colecciones vacias, True para los demas valores, como lo pueden ser listas,tuplas,set,diccionarios,etc


# Listas

valor=[]
res=bool(valor)
print(f"Valor: {valor} , El resultado es: {res}")

valor=["Nicolas",19,"ML","Data Scients","Python Full Stack Developer"]
res=bool(valor)
print(f"Valor: {valor} , El resultado es: {res}")


# Tuplas
valor=()
res=bool(valor)
print(f"Valor: {valor} , El resultado es: {res}")

valor=("Nicolas",19,"ML","Data Scients","Python Full Stack Developer")
res=bool(valor)
print(f"Valor: {valor} , El resultado es: {res}")

# Diccionarios
valor={}
res=bool(valor)
print(f"Valor: {valor} , El resultado es: {res}")

valor={"Nombre":"Nicolas",
       "Edad":19,
       "Profesion Futura 1":"ML",
       "Profesion Futura 2":"Data Scients",
       "Sueño por conseguir":"Python Full Stack Developer en IA y WEB"}

res=bool(valor)
print(f"Valor: {valor} , El resultado es: {res}")


# Tipo bool y sentencias de control

if bool((1,2,3,4,5)):
 print("Regreso verdadero")
else:
 print("Regreso falso")

if '1':
 print("Regreso verdadero")
else:
 print("Regreso falso")
    
variable=1    
while variable:
    print("EJecucio ciclo while")
    break
else:
    print("Fin ciclo while")        
    
    
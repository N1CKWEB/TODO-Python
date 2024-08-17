

# Generadores de números del 1 al 5:




def generadores_de_1_al_5():
  for numero in range(1,6):
       yield numero
       print('Se reanuda la ejecucion de la funcion')



# Utilizamos el generador
generador=generadores_de_1_al_5()

print(f"Objeto generador: {generador}")
print(f"El tipo del generador: {type(generador)}")

print('\n')

# Consumimos los valores del generador
for valor in generador:
    print(f"Numero producido por el generador: {valor}")


# Consumir a demanda

generador=generadores_de_1_al_5()

try:
  print(f"Consumimos a demanda::  {next(generador)}")
  print(f"Consumimos a demanda::  {next(generador)}")
  print(f"Consumimos a demanda::  {next(generador)}")
  print(f"Consumimos a demanda::  {next(generador)}")
  print(f"Consumimos a demanda::  {next(generador)}")
  print(f"Consumimos a demanda::  {next(generador)}")
except StopIteration as e:
  print(f'Ocurrio un error {e}')

# Otra forma de consumir un generador, usando un ciclo "while"
generador=generadores_de_1_al_5()

while True:
  try:
     valor=next(generador)  
     print(f'Impresion del valor generado: {valor}')
  except StopIteration as e:
     print(f'Se termino de iterar el generador ')
     break








# Manejo de valores infinitos

# Modulo de math

import math 
from decimal import Decimal

# inf- representa el valor de infinito
infinito_positivo=float('inf')

print(f"Infinitivo positivo: {infinito_positivo}")

print(f'Es infinito?  {math.isinf(infinito_positivo)}')


infinito_negativo=float('-inf')


print(f"Infinitivo negativo: {infinito_negativo}")

print(f'Es infinito?  {math.isinf(infinito_negativo)}')


# Manejo de Valores Infinitos - parte 2

# Utilizando el modulo de math: 

infinito_positivo=math.inf

print(f"Infinitivo positivo: {infinito_positivo}")

print(f'Es infinito?  {math.isinf(infinito_positivo)}')

infinito_negativo=-math.inf

print(f"Infinitivo negativo: {infinito_negativo}")

print(f'Es infinito?  {math.isinf(infinito_negativo)}')


# Utilizando el modulo de decimal

infinito_positivo=Decimal('Infinity')

print(f"Infinitivo positivo en decimal: {infinito_positivo}")

print(f'Es infinito en decimal?  {math.isinf(infinito_positivo)}')

infinito_negativo=Decimal('-Infinity')

print(f"Infinitivo negativo en decimal: {infinito_negativo}")

print(f'Es infinito en decimal?  {math.isinf(infinito_negativo)}')












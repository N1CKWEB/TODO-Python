
# Tipo NaN (Not a number) en python:


import math
from decimal import Decimal

# No es sensible a mayusculas/minusculas el tipo NaN
# NaN es un tipo de dato numérico indenifido
a=float('NaN')

print(f"A: {a}")

print(f"Es Nan (not a number) ?: {math.isnan(a)}")

a=Decimal('NaN')

print(f"A: {a}")
print(f"Es Nan (not a number) ?: {math.isnan(a)}")














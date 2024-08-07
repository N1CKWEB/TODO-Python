# Profurizando en el tipo float en python



a=3.0
print(f"a:{a:.2f}")


# Constructor de tipo float

a=float( '10' )
print(f"a:{a:.3f}")


# Notación exponencial (valores positivos o negativos )

a=3e5
a=3e-5
# print(f"a: {a:.5f}")



# Cualquier calculo que involucre un float, todo se promueve a float


a=4.0+5
print(a)

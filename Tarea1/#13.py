"""
Dada una lista con elementos repetidos como [5, 3, 5, 2, 3, 1], crea una nueva lista con elementos
únicos y ordenados.
"""

Lista=[5, 3, 5, 2, 3, 1,2,1,3,4,5,6,4,5]

R=set(Lista)
Resultado=list(sorted(R))
print(Resultado)
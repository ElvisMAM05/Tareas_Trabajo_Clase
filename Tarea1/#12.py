"""
Usa map() para redondear los números de una lista como [4.3, 5.7, 8.2].
"""

Lista=[4.3, 5.7, 8.2,9.6]

Orden=map(lambda n: round(n),Lista)
R=list(Orden)
print(R)
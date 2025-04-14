"""
Dada una lista de tuplas como [("Juan", 25), ("Ana", 20), ("Luis", 30)], ordénala por edad
"""

Tupla=[("Juan", 25), ("Ana", 20), ("Luis", 30)]

Resultado=sorted(Tupla, key=lambda n:n[1])
R=list(Resultado)
print(R)
"""
Dada una lista de palabras en minúsculas, usa map() para convertir todas las palabras a mayúsculas.
"""

palabras=["hola","adios","bueno","malo","salud","rata","rato"]

Palabras_M=map(lambda n:n.upper(),palabras)

List=list(Palabras_M)

print(List)
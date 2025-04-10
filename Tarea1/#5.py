"""
Crea un programa en Python que reciba un diccionario con valores decimales y devuelva un nuevo
diccionario con los valores redondeados.
"""

Numeros_decimales={
    "a":2.23,
    "b":4.56,
    "c":43.56,
    "d":356.543,
    "e":435.4356,
}
Lista=list(Numeros_decimales)

for Numero in Numeros_decimales:    Nuevo_numero= round(Numero)

print(Nuevo_numero)
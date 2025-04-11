"""
Crea un programa en Python que reciba un diccionario con valores decimales y devuelva un nuevo
diccionario con los valores redondeados.
"""


def Numeros_Ordenados(Numeros):
    
    Numero_Redondeado={key:round(valor)for key, valor in Numeros.items ()}
    return Numero_Redondeado  
    
    
Numeros_decimales={
    "a":2.23,
    "b":4.56,
    "c":43.56,
    "d":356.543,
    "e":435.4356,
    }
Lista_Actualizada=Numeros_Ordenados(Numeros_decimales)
print(Numeros_decimales)
print(Lista_Actualizada)    

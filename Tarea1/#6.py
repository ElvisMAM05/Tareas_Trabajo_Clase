"""
Dada una lista de palabras, usa map() para obtener una lista con la longitud de cada palabra.
"""


Lista=["Nitro","Hola","Shory","Trampa","Infeliz","Hello","Adios"]
Longitud_M=map(lambda n: len(n),Lista)
print(list(Longitud_M))


"""
Otra manera de hacerlo 
"""


Lista=["Nitro","Hola","Shory","Trampa","Infeliz","Hello","Adios"]

def Longitud(palabra):

    return len(palabra)

Longitud_M=map(Longitud,Lista)

print(list (Longitud_M))   

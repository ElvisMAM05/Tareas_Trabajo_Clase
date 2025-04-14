"""
Dada una lista de palabras, usa filter() para eliminar todas las que tengan menos de 5 letras.
"""


Lista=["Nitro","Hola","Shory","Trampa","Infeliz","Hello","Adios,ola,gato"]
Longitud_M=filter(lambda n: len(n)>=5,Lista)
print(list(Longitud_M))
"""
Dada una lista de números, usa map() para crear una nueva lista con cada número triplicado.
"""

numeros=[2,4,5,6,7,8,9,98,76]
Resultado= map(lambda n:n*3,numeros)
Resultado_Total= list(Resultado)
print(Resultado_Total)
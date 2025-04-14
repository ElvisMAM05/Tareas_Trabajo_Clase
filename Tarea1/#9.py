"""
Dada una lista de números (positivos y negativos), filtra solo los positivos.
"""

Lista=[1,2,3,4,5,6,7,-6,-7,-5,-8,-6]

Positivos=filter(lambda n: n>=0,Lista)
Resultado=list(Positivos)
print(Resultado)
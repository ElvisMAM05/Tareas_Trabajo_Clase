"""
Dada una lista de temperaturas en grados Celsius, conviértelas a Fahrenheit usando la fórmula:
F = C * 9/5 + 32
"""

Lista=[98,67,65,345,687,345]
Resultado=map(lambda x:x*9/5+32,Lista)
R=list(Resultado)
print(R)


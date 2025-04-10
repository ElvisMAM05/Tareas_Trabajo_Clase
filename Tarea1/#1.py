"""
Dada una lista de números, utiliza filter() para obtener una nueva lista que contenga únicamente los
números pares.
"""






Numeros=[1,2,3,4,5,6,7,8,9,10]

listaPar = filter(lambda n:n%2==0,Numeros)

print(list(listaPar))
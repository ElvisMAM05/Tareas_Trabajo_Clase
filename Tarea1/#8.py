""""Convierte una lista como ["1", "2", "3"] a enteros usando map().
"""""
Lista=["1","2","3","4","5","6","7","8"]

Enteros=map(lambda ent:int(ent),Lista)

Resultado=list(Enteros)
print(Resultado)

for valor in Resultado:
    print(f"Valor: {valor}, Tipo: {type(valor)}")

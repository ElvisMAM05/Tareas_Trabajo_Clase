def palindromo(palabra):
    
    palondromo= "".join(reversed(palabra))
    if palondromo.lower()==palabra.lower():
        Resultado=True
        print(Resultado)
    else:
        Resultado=False
        print(Resultado)
    
    return Resultado
    
        
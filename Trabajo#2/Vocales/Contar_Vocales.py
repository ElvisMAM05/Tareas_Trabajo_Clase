
def vocales_C(palabra):
    
    vocales=["a","e","i","o","u"]
    vocales_Count=0
    for e in palabra:
        if e in vocales:
            vocales_Count +=1
    return vocales_Count
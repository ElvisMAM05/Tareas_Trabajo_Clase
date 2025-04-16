def suma(a,b):
    total=a+b
    return total

def resta(a,b):
    total= a-b
    return total
    

def div(a,b):

    try:
        total= a/b
    except ZeroDivisionError:
        print("No se puede dividir entre cero cariño")
        
        
    return total
    
def mult(a,b):
    total= a*b
    return total
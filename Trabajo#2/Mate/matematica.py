
def esprimo(numero):
    
    if numero<=1:
        print("el número 1 y los números negativos no son primos ")
        return False
    for n in range (2,int(numero**0.5)+1):
        if numero% n == 0:
            print("El número no es primo")
            return False 
    print("es primo")
    return True 
  
esprimo(2)

def factorial(n):


    
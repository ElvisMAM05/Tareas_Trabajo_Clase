from __future__ import print_function
# The Caesar Cipher Algorithm

def main():
    message = input("Introducir Mensaje: ").upper()


    translated = encdec(message)
   
    print(("Mensaje Cifrado:", translated))
   
        
def encdec(message):
    translated = ""
    LETTERS    = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            vol= num+1
            translated += LETTERS[vol] 
    return translated

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
    input()
'''

1. Scrivere le seguenti funzioni:
• all_the same(x, y, z) che ritorna True se tutti gli argomenti sono
uguali;
• all_different(x, y, z) che ritorna True se tutti gli argomenti sono
diversi;
• all_sorted(x, y, z) che ritorna True se tutti gli argomenti sono in
ordine crescente.

'''


def main():

    x = int(input("inserire x"))
    y = int(input("inserire y"))
    z = int(input("inserire z"))

    #controlli tramite funzioni

    all_the_same(x,y,z)
    all_different(x,y,z)
    all_sorted(x,y,z)





#corpo delle funzioni

def all_the_same(x,y,z):

    if x==y and y==z:

        return bool true
    
    else :

        return bool false

        

def all_different(x,y,z):

    if x!=y and y!=z :

        return bool true

    else :

        return bool false


def all_sorted(x,y,z):

    if x<y and y<z:

        return bool true

    else :

        return bool false


main()










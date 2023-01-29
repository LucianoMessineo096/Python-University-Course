'''

Scrivi una funzione a cui viene passata una parola e riconosce se si tratta di un palindromo
 (parole che si leggono uguali anche al contrario) oppure meno.

'''


def main():



    stringa = str(input("inserire la stringa\t"))


    palindromo(stringa)


################################################################


def palindromo(stringa):

    if stringa==stringa[::-1] :  #utilizzo il reverse della stringa , infatti se la stringa è uguale alla sua inversa allora sono palindrome

        print("sono palindromi")

    else :

        print("non sono palindromi")










main()
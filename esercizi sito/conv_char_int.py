'''
    Scrivi una funzione che data in ingresso una lista A contenente n parole,
    restituisca in output una lista B di interi che rappresentano la lunghezza delle parole contenute in A.

'''


def main():

    l1=[]

    print("inserire parola nella lista")


    for i in range(10):

        l1.append(str(input()))

    l2=len_str(l1)

    for elm in l2:

        print(l2[elm])

    


def len_str(l1):

    l2=[]

    for elm in l1:

        l2.append(len(elm))

        
        
    return l2

    




main()
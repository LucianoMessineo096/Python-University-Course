'''

Inserisci n elementi nella lista da tastiera. Al termine dell’inserimento visualizzare gli elementi con il relativo indice.

'''

def main():

    l1=[]


    #inserimento

    print("inserire elementi nella lista\n")

    for i in range(10):

        l1.append(int(input()))

    

    for j in range(len(l1)):

        print("elemento" , l1[j] )

        print("posizione:",  l1.index(l1[j]))

main()


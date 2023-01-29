'''

Popolare una lista di n elementi con i primi n multipli di 5 escludendo lo zero.
Dopo aver terminato l’inserimento visualizzare in output i valori della lista e il relativo indice.

'''

def main():

    # inserimento

    l1=[]

    for i in range(31):

        if i%5==0:

            l1.append(i)

    for j in range(len(l1)):

        print("elemento" , l1[j] )

        print("posizione:",  l1.index(l1[j]))

main()


'''

Popolare una lista di n elementi con i primi n numeri pari. 
Dopo averli inseriti visualizzare in output i valori memorizzati nella lista e la loro posizione.

'''

def main():

    l1=[]


    #inserimento 


    for j in range(10):

        if j%2==0:

            l1.append(j)

    #print

    for i in range(len(l1)):

        print("elemento" , l1[i] )

        print("posizione:",  l1.index(l1[i]))
    





main()
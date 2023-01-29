'''
Creare una lista di n numeri decimali. 
Dopo aver inserito tutti gli elementi, sommare gli elementi con indice pari e con indice dispari separatamente. 
Infine visualizzare in output le due somme ottenute.

'''

def main():

    l1=[]

    somma_pari=0
    somma_dispari=0

    print("inserire valori nella lista")

    for i in range(10):

        l1.append(int(input()))

    for j in range(len(l1)):

        if l1[j]%2==0:

            somma_pari+=l1[j]

        else :

            somma_dispari+=l1[j] 

    print("somma numeri pari", somma_pari)

    print("somma dispari",somma_dispari)  

main()


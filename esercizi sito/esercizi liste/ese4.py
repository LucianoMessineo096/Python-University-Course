'''

Creare una lista di n numeri decimali, sommarli e fare la media. 
Dopo l’inserimento sommarli e visualizzare in output la somma e la media

 '''

def main():

    l1=[]
    count=0
    somma=0

    print("inserire elementi lista")


    for i in range(10):

        l1.append(int(input()))

        somma+=l1[i]

        count+=1

    print("somma",somma)

    media=somma/count

    print("media",media)

main()
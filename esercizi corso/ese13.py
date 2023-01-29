'''

Scrivere un programma che implementi il cosiddetto Crivello di
Eratostene. Scegliere un numero intero n. Il programma deve calcolare
tutti i numeri primi fino ad n. Innanzitutto, inserire tutti i numeri da 2 ad
n all’interno di un set. Poi, eliminare tutti i multipli di 2 (eccetto 2); e
quindi 4, 6, 8, 10, ... . Cancellare quindi tutti i multipli di 3. E così via
fino ad arrivare a √n. I numeri restanti sono tutti primi.

'''
import math


def main():

    value_set=set() #crea un set vuoto

    value=int(input("inserire valore \n"))

    insert_values(value , value_set) # inserisce tutti i valori all'interno di value_set

    print(value_set)

    print("\n")

    value_set1=discard_two_multiples(value , value_set) # cancella tutti i multipli di due dal set

    
    print(value_set1)

    print("\n")

    value_set2=discard_tree_multiples(value , value_set1) # cancella tutti i multipli di 3 sal set

    print(value_set2)

    print("\n")


def insert_values(value , value_set):

    for i in range(1, value):

        i=i+1

        value_set.add(i)

    return value_set


def discard_two_multiples(value , value_set):

    value_set1 = {elem for elem in value_set if elem%2!=0}


    return value_set1


def discard_tree_multiples(value , value_set1):

    value_set2 = {elem for elem in value_set1 if elem%3!=0}


    return value_set2



main()



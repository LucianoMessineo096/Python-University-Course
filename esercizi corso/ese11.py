'''

Scrivere un programma che legga un file contenente due colonne di
numeri in virgola mobile e stampi la media di ciascuna colonna

'''

#variables

tot_column1=0
tot_column2=0
count_row=0

import os

print(os.getcwd())  #fornisce la current working directory

filename='input.txt'

#print(filename)

with open(filename , 'r') as f:

    for riga in f :

        riga=riga.rstrip() # rimuove il carattere di newline

       # print(riga)

        lista_parole = riga.split()

        print(lista_parole)

        num1=float(lista_parole[0])
        num2=float(lista_parole[1])

        tot_column1+=num1
        tot_column2+=num2

        count_row+=1


    print(f'media colonna 1', {tot_column1/count_row})
    print(f'media colonna 2', {tot_column2/count_row})


# ad ogni iterata lista_parole[i] conterrà l'elemento della riga nella posizione i-esima




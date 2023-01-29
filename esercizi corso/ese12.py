'''

Scrivere un programma che, dato un file di testo, stampi il numero di
caratteri, parole e righe in quel file.

'''

import os


def main():

    print(os.getcwd())

    print('numero di caratteri:\n')

    count_character()

    print('numero di parole:\n')

    count_word()

    print('numero di righe:\n')

    count_row()





def count_character():

    count_character=0
    

    with open('input2.txt' , 'r') as f :

        for row in f:

            list_word = row.split()
            
            for word in list_word:

                count_character+=len(word)

    f.close() # chiusura file 

    return print(count_character)



def count_word():

    count_word=0
    punteggiatura = " .,:;!?' \n"

    with open('input2.txt' , 'r') as f :

        for row in f:

            row=row.rstrip(punteggiatura)

            list_word = row.split()
            
            for word in list_word:

                count_word+=1

    f.close() # chiusura file 

    return print(count_word)




def count_row():

    count_row=0
    punteggiatura = " .,:;!?' \n"

    with open('input2.txt' , 'r') as f :

        for row in f:

            row=row.rstrip(punteggiatura)

            #print(row)

            if row !='':

                count_row+=1

    f.close() # chiusura file 

    return print(count_row)







main()



'''

Scrivere un programma che mantenga un dizionario in cui le chiavi sono
nomi di studenti, e i valori le valutazioni ricevute per un esame. Il
programma deve chiedere all’utente se desidera aggiungere o rimuovere
studenti, modificare valutazioni, o stampare tutte le valutazioni.


'''

def main():


    print("***GESTIONE STUDENTI***\n")

    dictionary = {} # definizione di un dizionario vuoto


    #menu'

   
    print("1.AGGIUNGERE STUDENTI\n2.RIMUOVERE STUDENTI\n3.MODIFICARE VALUTAZIONI\n4.STAMPARE LE VALUTAZIONI\n")

    for i in range(100) :

        print("menu' di scelta\n")
    
        choice = int(input())

        if choice==1 :

            add_student(dictionary)

        elif choice==2 :

            remouve_student(dictionary)

        elif choice==3 :

            modify()

        elif choice==4 :

            see_all(dictionary)

        elif choice==404 :

            break 

        else :

            print("scelta errata")



        
    




    

#############################################################################################################

def add_student(dictionary):

    print("inserire nome studente e valutazione")

    name = str(input())

    evaluation = int(input())


    if evaluation>18 and evaluation<=30 :

        dictionary[name] = evaluation

        return dictionary

    else :

        print("valutazione al di sotto della soglia minima , verrà impostata a NON IDONEO")

        negative_evaluation = "NON IDONEO"

        dictionary[name] = negative_evaluation

        return dictionary


    


def see_all(dictionary) :

    for key in dictionary:


        print(key, ':', dictionary[key])



    '''

    for (key, value) in dictionary.items():

        print(key, ':', value)
        
    '''

def remouve_student(dictionary):

    print("inserire nome studente")

    name = str(input())


    if name in dictionary :

        dictionary.pop(name)

    else : 

        print("la persona non è presente in elenco")




    return dictionary






main()
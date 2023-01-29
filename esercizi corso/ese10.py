'''

. Scrivere questo insieme di funzioni per elaborare liste di numeri interi,
e scrivere un main che testi tutte le funzioni implementate:
• scambiare il primo e l’ultimo elemento della lista
• shiftare tutti gli elementi di una posizione verso destra, e far sì che
l’ultimo elemento diventi il primo della nuova lista
• rimpiazzare tutti gli elementi pari con 0
• ritornare il secondo elemento più grande nella lista
• calcolare la somma degli elementi di una lista, escludendo
l’elemento più piccolo
• ritornare True se la lista è ordinata in senso crescente
• ritornare True se la lista contiene due elementi adiacenti duplicati
• ritornare True se la lista contiene elementi duplicati (non per forza
adiacenti).

'''

#corpo

def main () :

    l1=[1,2,3,4,5,6,6,7]
    l2=[6,3,4,2,2,1,5,4]

    print("lista 1\n", l1)
    print("lista 2\n", l2)

    #swap_first_last(l1,l2)

    #print("swap first and last element : \n" , l1,l2)

    #right_shift(l1,l2)

    #print("right_shift" , l1)

    #switch_odd_element_with_zero(l1,l2)

    # print(l1)

    #second_biggest_value(l1,l2)

    #list_element_sum(l1,l2)

    #ascending_order(l1,l2)

    #equals_adjacents_element(l1,l2)






#definizione funzioni

def swap_first_last(l1,l2):

    #scambia primo ed ultimo elemento della lista

    
    l1[0], l1[len(l1)-1] = l1[len(l1)-1], l1[0]
    l2[0], l2[len(l2)-1] = l2[len(l2)-1], l2[0]

    return l1,l2

#def right_shift(l1,l2):

    #shiftare tutti gli elementi di una posizione verso destra, e far sì che
    #l’ultimo elemento diventi il primo della nuova lista

    
def switch_odd_element_with_zero(l1,l2):

    for i in range(len(l1)):

        if l1[i]%2==0 :

            l1[i]=0

    for i in range(len(l2)):

        if l2[i]%2==0 :

            l2[i]=0
    
    return l1,l2


def second_biggest_value(l1,l2):


    l1.sort(reverse=False)# ordinamento in ordine ascendente

    #print(l1)

    second_max1=l1[len(l1)-2]

    print(second_max1)

    l2.sort(reverse=True) #ordinamento in ordine discendente

    #print(l2)

    second_max2=l2[1]

    print(second_max2)

    
def list_element_sum(l1,l2):

    #calcolare la somma degli elementi di una lista, escludendo l’elemento più piccolo

    l1.sort(reverse=True)
    l2.sort(reverse=True)

    somma_1=0
    somma_2=0

    for i in range(len(l1)-1):

        somma_1+=l1[i]

    for i in range(len(l2)-1):

        somma_2+=l2[i]
        

    print(somma_1, somma_2)



def ascending_order(l1,l2):

    count_1=0
    count_2=0

    #analisi lista 1 

    for i in range(len(l1)-1):

        if l1[i]<=l1[i+1] : #metto <= per includere gli elementi duplicati

            count_1+=1

            #print(count_1)

       

    if count_1==len(l1)-1:

         print("TRUE")

    else: 

        print("FALSE")
        
    #analisi lista 2
   
    for i in range(len(l2)-1):

        if l2[i]<=l2[i+1] : #metto <= per includere gli elementi duplicati

            count_2+=1

            #print(count_2)

       

    if count_2==len(l2)-1:

         print("TRUE")

    else: 

        print("FALSE")
               

def equals_adjacents_element(l1,l2):

    count_1=0
    count_2=0

    #analisi lista 1 

    for i in range(len(l1)-1):

        if l1[i]==l1[i+1] : #metto <= per includere gli elementi duplicati

            count_1+=1

            #print(count_1)

       

    if count_1>=1:

         print("TRUE")

    else: 

        print("FALSE")
        
    #analisi lista 2
   
    for i in range(len(l2)-1):

        if l2[i]==l2[i+1] : #metto <= per includere gli elementi duplicati

            count_2+=1

            #print(count_2)

       

    if count_2>=1:

         print("TRUE")

    else: 

        print("FALSE")




    
     

main()
    


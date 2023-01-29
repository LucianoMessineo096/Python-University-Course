'''

Scrivi una funzione che, data una lista di numeri, fornisce in output un istogramma basato su questi numeri, usando asterischi per disegnarlo.

Data ad esempio la lista [3, 7, 9, 5], la funzione dovrà produrre questa sequenza:

***

*******

*********

*****

'''

def main():

    l1=[]

    print("inserire nella lista 10 numeri")


    for i in range(10):

        l1.append(int(input()))

    
    for elm in l1 :

        print("*"*elm)

'''
    for elm in l1 :

        print(l1[elm])

'''


    



main()



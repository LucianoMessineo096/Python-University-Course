'''

Scrivi una funzione "moltiplicatrice" che moltiplica tra loro tutti gli elementi di una lista di numeri.

'''


def main():

    lista = []

    num_input=int(input("how much values want you insert?\n"))

    insert_list(lista , num_input)

    print_list(lista)

    multiplication = multiply_all(lista , num_input)

    print(multiplication)





#############################################################################


def print_list(lista):

    for i in range(len(lista)):

        print(lista[i])


def insert_list(lista , num_input):

    for i in range(num_input):

        val = int(input("val\t"))

        lista.append(val)


def multiply_all(lista, num_input):


    multiplication=1

    for i in range(num_input):

        multiplication = multiplication*lista[i]

    print("il prodotto totale e'")


    return  multiplication





        
        






main()


'''

Scrivere la funzione middle(string) che ritorna una stringa contenente il
carattere centrale in string se la dimensione della stringa è dispari,
altrimenti ritorna i due caratteri centrali se la dimensione è pari. Ad
esempio, middle('middle') deve ritornare la stringa 'dd'.

'''



def main() :


    string = str(input("inserire la stringa\n"))

    middle(string)

 



def middle(string) :


    if len(string) % 2 !=0 :

        index = int(len(string)/2)

        result = string[index]

        
        return print(result)

    else :

        





main()



'''

Implementare una classe Studente. Uno studente ha un nome, e un
punteggio totale conseguito nei quiz. Scrivere un costruttore
appropriato e i metodi aggiungi_quiz(punteggio) e punteggio_medio().
Per l’ultimo metodo occorrerà tenere traccia del numero di quiz che lo
studente ha sostenuto.


'''

class Studente :

    #### costruttore ####

    def __init__(self , matricola , nome , cognome , punteggio=0):

        self.matricola = matricola
        self.nome      = nome
        self.cognome   = cognome
        self.punteggio = punteggio
        self.n_quiz    = 0


    ###### metodi della classe ######

    def fullname(self):

        return self.matricola +" "+ self.nome +" "+ self.cognome +" "+ str(self.punteggio) +" "+ str(self.n_quiz)


    def aggiungi_quiz(self , punteggio):

        self.punteggio += punteggio
        self.n_quiz +=1


    def punteggio_medio(self) :

        media = self.punteggio / self.n_quiz

        return media


#######################################################################################################################



def main():

    lista =[]

    for i in range(100):

        print("1.INSERIRE STUDENTE\t2.RIMUOVERE STUDENTE\t3.STAMPA LISTA STIDENTI\t4.ESCI")

        choice = int(input())


        if choice == 1 :

            lista = add_student()

            choice2 = int(input("1.continua\t2.esci"))

            if choice2==1 :

                continue

            else :

                break

        elif choice == 2 :

            remouve_student()

            choice2 = int(input("1.continua\t2.esci"))

            if choice2==1 :

                continue
            
            else :

                break


        elif choice == 3 :

            print_list(lista)

        else :

            break


## metodi ##


def add_student():

    lista =[]

    matricola = str(input("\nmatricola:\t"))
    nome      = str(input("\nnome:\t"))
    cognome   = str(input("\ncognome:\t"))
    punteggio = int(input("\npunteggio:\t"))



    studente = Studente(matricola , nome , cognome , punteggio)


    lista.append(studente)


    return lista


def print_list(lista):


    for studente in lista :

        print(studente.fullname())








main()









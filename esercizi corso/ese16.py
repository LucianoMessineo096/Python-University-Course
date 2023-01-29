'''

Implementare una classe Impiegato. Un impiegato ha un nome, un
cognome, un indirizzo email e uno stipendio. Tutti gli oggetti della
classe Impiegato condividono una certa quota percentuale di
incremento stipendio annuale, che viene fissata dall’azienda.
Implementare il metodo aumento per applicare l’aumento annuale di
stipendio. Tenere traccia del numero di impiegati dell’azienda.


'''

class Impiegato :


    def __init__(self , nome , cognome , email , stipendio):

        self.nome      = nome
        self.cognome   = cognome
        self.email     = email
        self.stipendio = stipendio

    def aumento(self , stipendio):

        incremento = (stipendio * 7)/100

        return nuovo_stipendio = stipendio+incremento

    def n_impiegati(self):

        self.num +=1




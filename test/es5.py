# La classe StudenteTriennale è una classe figlia della classe Studente del precedente esercizio. 
# Sostituire i frammenti di codice ? e ?? affinchè la classe StudenteTriennale funzioni correttamente:
class Studente:

    def __init__(self, nome, cognome, matricola):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola

    def func4(self):
        x = 1
        if 'a' in self.nome:
            x += 2
        if 'e' in self.cognome:
            x += 1
        n = int(self.matricola[-3])
        return (n + x) % 4


class StudenteTriennale(Studente):

    def __init__(self, nome, cognome, matricola, lista_materie_a_scelta):
        super().__init__(nome, cognome, matricola)
        self.lista_materie_a_scelta = lista_materie_a_scelta

    def print_materie_a_scelta(self):
        for materia in self.lista_materie_a_scelta:
            print(materia)

s = StudenteTriennale('test', 'prova', '123', ['A', 'B'])
s.print_materie_a_scelta()
print(s.nome)
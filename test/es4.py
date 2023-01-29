# In questa classe, il metodo func4 elabora gli attributi nome cognome e matricola dell'oggetto invocante. 
# Passando i propri dati in input, indicare l'output della funzione:
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

s = Studente('Andrea', 'Giammanco', '0123456')
res = s.func4()
print(res)
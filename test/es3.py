# Si supponga che filename contenga il percorso di un file di testo con diverse righe al suo interno. 
# Questo programma accumula in una lista tutti i primi caratteri delle diverse righe. 
# Sostituire i tre diversi frammenti, ?, ?? e ???, affinché il programma raggiunga il suo scopo:
filename = 'test.txt'
punteggiatura = ',.;!'
lista_caratteri_prima_posizione = []
lista_caratteri_prime_due_posizioni = []
with open(filename, "r") as f:
    for riga in f:
        print(riga.rstrip().strip(punteggiatura))
        lista_caratteri_prima_posizione.append(riga[0])
        lista_caratteri_prime_due_posizioni.append(riga[0:2])

print(lista_caratteri_prima_posizione)

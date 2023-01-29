import os

count_caratteri = 0
count_caratteri_no_punct = 0
count_parole = 0
count_righe = 0

filename = 'input2.txt'
with open(filename, 'r') as f:
    for riga in f:
        riga = riga.rstrip()
        punteggiatura = ".,;!?'"
        riga_senza_punteggiatura = riga.strip(punteggiatura)
        # contando spazi bianchi
        #count_caratteri += len(riga)
        lista_parole = riga.split()
        count_parole += len(lista_parole)
        if riga != '':
            count_righe += 1
        for singola_parola in lista_parole:
            count_caratteri += len(singola_parola)

        lista_parole_no_punteggiatura = riga_senza_punteggiatura.split()
        for singola_parola_no_punct in lista_parole_no_punteggiatura:
            count_caratteri_no_punct += len(singola_parola_no_punct)

print(f'Il file contiene {count_caratteri} caratteri, {count_caratteri_no_punct} caratteri senza punteggiatura')
print(f'{count_parole} parole e {count_righe} righe.')


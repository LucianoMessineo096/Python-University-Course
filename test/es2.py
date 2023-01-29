# Questa funzione riceve in ingresso il proprio nome, cognome e matricola sotto forma di stringhe. 
# Indicare quale output restituisce la funzione inserendo tali dati:
def func2(nome, cognome, matricola):
    my_dict = {'nome': nome, 
               'cognome': cognome, 
               'matricola': (int(matricola[-1]) % 4)}
    n = int(matricola[-2]) % 3
    l = ['nome', 'cognome', 'matricola']
    try:
        print(int(my_dict[l[n]]) + 1)
    except:
        print("Errore.")

    for var in my_dict:
        print(var)
        print(my_dict[var])

    for key, value in my_dict.items():
        print(key, '->', value)

matricola = '0123456'
func2('test', 'prova', matricola)
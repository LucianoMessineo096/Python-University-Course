# Quale output restituisce la seguente funzione fornendo in input la propria matricola?
def func1(matricola):
    l1 = [int(i) for i in matricola if (int(i) % 2) == 0]
    l2 = [int(i) for i in matricola if (int(i) % 2) == 1]
    s1 = 0
    for i in l1:
        s1 += i
    s2 = 0
    for j in l2:
        s2 += j
    s = abs(s1 - s2)
    return s % 4

matricola = '0123456'
print(func1(matricola))
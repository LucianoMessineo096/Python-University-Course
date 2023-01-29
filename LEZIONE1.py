#################################LEZIONE 1 PT 1##############################################################à

print("hello world")
print(3+4) #valuta prima l'espressione e poi la funzione#   #commento#

print("il risultato e:", 6+7)

print()
print("hello") 


 #errore di indentazione#
'''
 print("hello")
  print()
'''

#non stampa niente

x=2
if x>5:
    print("hello")
    print("world")

#stampa world

if x>5:
    print("hello")
print("world")

#case sensitive

'''
#Print differente da print
'''

print()
print()

####################ESE LEZIONE PARTE 1##########################################################################################

#ese 1 scrivere un programma che visualizzi tre stringhe su 3 righe consecutive

print("fight club \narancia meccanica \nforrest gump")

print()
print()

#ese2 scrivere un programma che visualizzi sullo schermo il proprio nome all'interno di un rettangolo 

print("+---------+\n| Luciano |\n+---------+")

print()
print()

#scrivere un programma che visualizzi la somma dei primi 10 numeri interi positivi

print("la somma dei primi 10  umeri interi positivi e' :", 1+2+3+4+5+6+7+8+9+10)

##############################################################################################################################

######################################### LEZIONE 1 PT 2 ##########################################################################

# VARIABILE = LOCAZIONE DI MEMORIA HE CONTIENE UN VALORE
 
# OPERATORE DI ASSEGNAZIONE x=3  [NOME OPERANDO]=[VALORE] NON E' NECESSARIO DEFINIRE LA VARIABILE

# IL TIPO E' ASSOCIATO AL TIPO DI VARIABILE 

taxRate= 3 # tipo int 

gg= "non tassabile"  # tipo string 


# per verificare il tipo si usa la funzione type

print()
print()

print("il tipo della variabile taxRate e':", type(taxRate))

#conversione da un tipo ad un altro
'''
x=int(x)
x=float(x)
x=str(x)
'''

taxRate='10' 
print(taxRate)

print(type(taxRate))

taxRate=int(taxRate)
print(type(taxRate))
print(taxRate)

print()
print()

#assegnazioni multiple

x,y,z =3,6,9

print(x,y,z)

#swap

x, y=y, x

print("x e y swappate")

print(x,y,z)



############################### OPERAZIONI ARITMETICHE ###########################################################

print()
print()





print("divisione tra interi:", 9/2)

print("divisione tra interi solo parte intera:", 9//2)

print("resto della divisione:", 9%2)

print("elevamento a potenza:", 3**3)


# espressione su piu righe 

'''
c =(-b + (a**b)) \
/ (2*a)

'''

# valore assoluto

abs(-389)

#intero piu vicino

round(3.369)

#intero piu vicino con  numero di cifre per la parte frazionaria a piacere

round(3.369 ,2)  #ove due e' il numero di cifre desiderate per la parte frazionaria


# le funzioni min e max restituiscono il valore minimo e massimo di un insieme

min(1,2,3,4)
max(1,2,3,4)


# utilizzo del modulo math

from math import sqrt

sqrt(9)

#oppure si puo scrivere

import math

math.sqrt(9)


print()
print()


######################### STRINGHE ##########################################################################################

# PER ACCEDERE AI SINGOLI CARATTERI DI UNA STRINGA 

string='abcdef'
print(string[0] , string[1])

#con indici negativi parto dalla fine 

print(string[-1], string[-2])

# lunghezza di una stringa

print(len(string))

# SLICING (selezionare una sottostringa)
'''
string[start : end]

'''

print("slicing" , string[0:2],string[2:4])

#concatenamento
s1='hello'
s2='world'
print(s1 + ' ' + s2)


#concatenamento stringa e numero

name = 'agent' + str(1729)

print(name)

#ripetizione di una stringa

riga ='-' *50  #l 'operatore * indica quante volte la stringa si deve ripetere

# upper

ciaone= 'ciao'.upper()

print(ciaone)

print()
print()

#replace

name ='mario rossi'

name= name.replace("mario" , "luigi")
print(name)

# input utente

name= input("inserisci il tuo nome")


age= int(input("inserire eta':")) # viene effettuata la conversione dell'input 

print()
print()

# segnaposto

print('segnaposto')

name2= 'claudio'

print("ciao {}. tutto bene?" .format(name2)) 

print()
print()

#meccanismo giustificazione

print('giustificato')

print('{:20} world'.format('Hello'))
print('{:>20} world'.format('Hello'))
print('{:^20} world'.format('Hello'))
print('{:*>20} world'.format('Hello'))

print()
print()

#f-strings

print('f-strings')

name, surname , age='mario','rossi',33
print(f'ciao, mi chiamo{name} {surname} , ho {age} anni')



##################### esercizi lezione 2 ################################################################################################

#ese1 chiedete all'utente di inserire due numeri interi e di stamparne somma e differenza, prodotto e media,distanza(valore assoluto della differenza), minimo e massimo
'''
num1= int(input("inserire valore 1: "))
num2= int(input("inserire valore 2: "))

import math
somma=num1+num2
differenza=num1-num2
prodotto=num1*num2
media=(num1+num2)/2
distanza=abs(differenza)
m=min(num1,num2)
M=max(num1,num2)

print('somma'+ str(somma) + ' ' + 'differenza' + str(differenza) + ' ' + 'prodotto' + str(prodotto) + ' ' + 'media' + str(media) + ' ' + 'distanza' + str(distanza))
print('minimo'+ str(m) + ' ' + 'massimo' + str(M))

OK
'''

#ese2 chiedere all'utente la lunghezza dei lati di un rettangolo e poi stampare area perimetro e lunghezza della diagonale
'''
baseM=int(input("inserire lunghezza base maggiore: "))
basem=int(input("inserire lunghezza base minore: "))

print("area : ", (baseM*basem))
print("perimetro: ", (2*baseM)+(2*basem))

import math

diagonal_lenght=math.sqrt((baseM**baseM)+(basem**basem))
print("lunghezza diagonale : " , diagonal_lenght)

OK
'''

#ese3 chiedere all'utente di inserire un numero tra 10.000 e 99.999 richiedendo esplicitamente una virgola separatirce delle migliaia.poi stampare il numero senza virgola


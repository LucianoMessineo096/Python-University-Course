'''
scrivere un programma che legga 3 numeri e stampi
"crescenti" se sono in ordine strettamente crescente
"decrescenti" se in ordine strettamente decrescente
"nessuna delle due " altrimenti
'''

num1=int(input("inserire il 1 numero: \n "))
num2=int(input("inserire il 2 numero: \n "))
num3=int(input("inserire il 3 numero: \n "))

if num1<num2 and num2<num3 :

    print("crescenti")

elif num1>num2 and num2>num3 :

    print("decrescenti")

else :

    print("nessuna delle due")

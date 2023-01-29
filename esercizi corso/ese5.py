'''
scrivere un programma che legga 3 numeri e stampi "tutti uguali"
se i loro valori sono gli stessi , "tutti differenti" se sono tutti
diversi, "nessuna delle due " altrimenti
'''

num1=int(input("inserire il 1 numero: \n "))
num2=int(input("inserire il 2 numero: \n "))
num3=int(input("inserire il 3 numero: \n "))

if num1==num2 and num2==num3 :

    print("tutti uguali")

elif num1!=num2 and num2!=num3 :

    print("tutti differenti")

else :

    print("nessuna delle due")



## scrivere un programma che dati n interi restituisca il massimo

a=int(input("integer 1:\n"))
b=int(input("integer 2:\n"))
c=int(input("integer 3:\n"))

if a<b :

    if b<c :

        print(a +" "+b+" "+c)

    elif c<b :

        print(a+" "+c+" "+b)

elif b<a :

    if a<c :

        print(b+" "+a+" "+c)

    elif c<a :

        print(b+" "+c+" "+a)

else c<a :

    if a<b :

        print(c+" "+a+" "+b)

    elif b<a :

        print(c+" "+b+" "+a)



            
            


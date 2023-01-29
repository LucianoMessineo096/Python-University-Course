##. Scrivere un programma che legga 3 stringhe e le ordini in senso lessicografico.

## input


stringa_1= str(input("inserire stringa 1"))
stringa_2= str(input("inserire stringa 2"))
nome_3= str(input("inserire stringa 3"))

#body

if stringa_1==stringa_2 and stringa_2==stringa_3 :

    print(stringa_1 +" "+  stringa_2 +" "+ stringa_3)

elif stringa_1>stringa_2 : ##macrocaso

    if stringa_2>stringa_3 :

        print(stringa_1+" "+stringa_2+" "+stringa_3)
    
    else nome_3>stringa_2 :

        print(stringa_1+" "+stringa_3+" "+stringa_2)

elif stringa_2>stringa_1 : ##macrocaso

    if stringa_1>stringa_3 :

        print(stringa_2+" "+stringa_1+" "+stringa_3)
    
    else stringa_3>stringa_1 :

        print(stringa_2+" "+stringa_3+" "+stringa_1)

else stringa_3>stringa_1 : #macrocaso

    if stringa_2>stringa_1 :

        print(stringa_3+" "+stringa_2+" "+stringa_1)

    else stringa_1>stringa_2 :

        print(stringa_3+" "+stringa_1+" "+stringa_2)



 ##end 
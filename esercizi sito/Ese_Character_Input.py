## crea un programma che chieda all'utente di inserire nome e eta.
## stampare un messaggio che chieda ad esso quanti anni avrà tra 100 anni

nome=str(input("inserire nome:\n"))
età=int(input("inserire età:\n"))

età100=int(input("quanti anni avrai tra 100 anni?:\n"))

if età100!=100+età :

   print("errore la tua età e' : " + str(100+età))

else :
    
   print("giusto la tua età sarà : " + str(età100))



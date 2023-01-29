'''

Scrivi una funzione a cui passerai come parametro una stringa, e che manderà in print una 
versione inversa (al contrario) della stessa stringa (ad esempio "abcd" diventerà "dcba")

'''

def main():

    stringa=str(input("inserire la stringa\t"))


    reverser(stringa)



#################################################


def reverser(stringa):

    print(stringa[::-1])

main()


'''

a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed

'''
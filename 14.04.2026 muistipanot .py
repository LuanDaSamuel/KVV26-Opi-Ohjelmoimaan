#String
nimi = "Samuel Sierra"
print(nimi)


print(nimi[0])
print(nimi[1])
print(nimi[2])
print(nimi[3])
print(nimi[4])
print(nimi[5])
print(nimi[6])
print(nimi[7])  
print(nimi[8])
print(nimi[9])
print(nimi[10])
print(nimi[11])
print(nimi[12])


etunimi= nimi[0:6]
sukunimi= nimi[7:13]

print("Etunimi:", etunimi)
print("Sukunimi:", sukunimi)

nimi.lower()
print(nimi.lower())
nimi.upper()
print(nimi.upper())

##Practicing
a = "Python"

len(a)
a[0]
a[1]
a[2]
a[3]
a[4]
a[5]

print(len(a))

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])

a.lower()
a.upper()

print(a.lower())
print(a.upper())

reversed_a = a[::-1]
print(reversed_a)


#if/ elif/ else
##Ehto rakenne "if"'
a = 20
b = int(input("Anna toinen luku: "))
if a > b:
    print("Luku", a, "on suurempi kuin luku", b)
elif a < b:
    print("Luku", a, "on pienempi kuin luku", b)
else:
    print("Luku", a, "on yhtä suuri kuin luku", b)

#Pieni Black Jack peli demo

##Coincidence number generator
import random
casinonumber = random.randint(1, 100)
my_number = int(input("Enter a number between 1 and 100: "))

print(my_number)
if my_number > casinonumber:
    print(f"Congratulations! You won. The number {my_number} was bigger than {casinonumber}.")
elif my_number == casinonumber:
    print(f"It's a tie! Both you and the casino chose the number {my_number}.")
else:
    print(f"Casino wins. The number {casinonumber} was bigger than {my_number}.")


##satunnaislukujen generointi
import random
kasino = 17
minun = random.randint(1,21)
print(f"Sait numeron {minun}")
#vertaillaan kumpi suurempi
if minun > kasino:
    print(f"Sinä voitit! {minun} on suurempi kuin {kasino}")
elif minun == kasino:
    print(f"Tasapeli.")
else:
    print(f"Kasino voitti!")


#Toistarakenne for/ while

import random

money=10
lost = 1
kasino = random.randint(1,10)

while money > 0:
    minun = int(input("Enter a number between 1 and 10: "))
    print(f"Sait numeron {minun}")
    #vertaillaan kumpi suurempi
    if minun > kasino:
        print(f"You won ! {minun} is bigger than {kasino}")
        money = money + 2 * lost
        print(f"You have {money} money left.") 
    elif minun == kasino:
        print(f"Draw.")
        money =  money + lost
        print(f"You have {money} money left.")
    else:
        print(f"Kasino voitti!")
        money -= lost
        print(f"You have {money} money left.")
    continue
print(f"Game over. You have {money} money left.")

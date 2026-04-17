#Tehtävä 1
import random

a = int(random.randint(1, 100))
b = int(random.randint(1, 100))
c = int(random.randint(1, 100))
#Tehtävä 2
z = [a, b, c]

print([x ** 2 for x in z])

if a < b < c:
            biggest = c
            smallest = a
            print(biggest, smallest)
elif a < c < b:
            biggest = b
            smallest = a
            print(biggest, smallest)
            biggest = c
            smallest = b
            print(biggest, smallest)
else:
            biggest = a
            smallest = c
            print(biggest, smallest)

#Tehtävä 2
import random

money=10
lost = 1
kasino = random.randint(1,36)

for i in range(10):
    minun = int(input("Enter a number between 1 and 36: "))
    print(f"You got number {minun}")
    #vertaillaan kumpi suurempi
    if minun > kasino:
        print(f"You won ! {minun} is bigger than {kasino}")
        money = money - lost + 36
        print(f"You have {money} money left.") 
    elif minun == kasino:
        print(f"Draw.")
        money =  money + lost - lost
        print(f"You have {money} money left.")
    else:
        print(f"Kasino voitti!")
        money -= lost
        print(f"You have {money} money left.")
    continue
print(f"Game over. You have {money} money left.")

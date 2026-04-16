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

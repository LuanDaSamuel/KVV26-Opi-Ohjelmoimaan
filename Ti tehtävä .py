#Tehtävä 1
a = input("Please enter your name: ")
len(a)
print(len(a))

#Tehtävä 2

a = float(input("Enter the first decimal number: "))
b = float(input("Enter the second decimal number: "))
c = a / b
print("The result of dividing", a, "by", b, "is:", c)

#Tehtävä 3

a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))
if a > b and a > c:
    print("The largest integer is:", a)
elif b > a and b > c:
    print("The largest integer is:", b)
else:
    print("The largest integer is:", c)

#Tehtävä 4

a = int(input("Please enter your age: "))

if a >= 13 and a <= 19:
    print("You are a teenager.")
elif a >= 20 and a <= 65:
    print("You are an adult.")
elif a < 13:
    print("You are a child.")
else:
    print("You are a senior.")

#Tehtävä 5

a = int(input("Please enter your score: "))

if a <= 1:
    print("Your number is 0")
elif a <= 3:
    print("Your number is 1")
elif a <= 5:
    print("Your number is 2")
elif a <= 7:
    print("Your number is 3")
elif a <= 9:   
    print("Your number is 4")
elif a <= 11:
    print("Your number is 5")
else:
    print("Your score is out of range")

#Tehtävä 6

a = int(input("Please enter the first score: "))
b = int(input("Please enter the second score: "))
c = int(input("Please enter the third score: "))
d= int(input("Please enter the fourth score: "))
e = int(input("Please enter the fifth score: "))


if (a > b and a > c and a > d and a > e) and (b < a and b < c and b < d and b < e):
    print("Your result is: ",  c + d  + e)
elif (b > a and b > c and b > d and b > e) and (c < a and c < b and c < d and c < e):
    print("Your result is: ",  a + d + e)
elif (c > a and c > b and c > d and c > e) and (d < a and d < b and d < c and d < e):
    print("Your result is: ",  a + b + e)
elif (d > a and d > b and d > c and d > e) and (e < a and e < b and e < c and e < d):
    print("Your result is: ",  a + b + d)
else:
    print("Your result is: ",  b + c + e)

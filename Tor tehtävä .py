#Tehtävä 1
import random
for i in range(10):
    a = random.randint(1, 100)
    print(a)

#Tehtävä 2
import random

a = random.randint(21, 100)

def guess_number():
    while True:
            guess = int(input("Guess the number between 21 and 100: "))
            if guess < a:
                print("Too low! Try again.")
            elif guess > a:
                print("Too high! Try again.")
            else:
                print("Congratulations! You've guessed the number!")
                break
guess_number()
print(f"The correct number was: {a}")

#Tehtävä 3

a = input("Enter your first name: ")

myfile = open("Samuj.txt", "w", encoding="utf-8")    
myfile.write(a)
myfile.close()
print("File created and data written successfully.")


#Tehtävä 4

#Input
a = input("Enter a number: ")

file_interger = open("integer.txt", "w")
file_float = open("float.txt", "w")



#Output
if a.find(",") >= 0:
    file_float = open("float.txt", "w")
    print("Saving successful.")
    print("The number is a float.")
    file_float.close()
else:
    file_interger = open("integer.txt", "w")
    print("Saving successful.")
    print("The number is an integer.")
    file_interger.close()

#Tehtävä 5




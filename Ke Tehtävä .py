#Tehtävä 1
a = int(input("Enter a number from 1 to 100: "))

for i in range (1, 101):
    print(f"(Your number: {i}, square: {i**2})")
    if i == a:
        break


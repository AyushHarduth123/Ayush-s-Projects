# For loops = a block of code that will execute its block of code a
# limited number of times
# can iterate through anything that can be iterable
for i in range(10, 100+1,5):
    print(f"{i}")
    print(f"\n")
# Through text too
for i in "Ayush":
    print(f"{i}")

print(f"Multiplication")
for i in range(1, 11):
    print(f"{i} x {i} = {i * i}")

print(f"Addition")
for i in range(10):
    print(f"{i} + {i} = {i + i}")

###################################################################
# Small count down timer program
import time

for i in range(10,0,-1):
    print(f"{i}")
    time.sleep(1)
print("HAPPY NEW YEAR")

###################################################################

# While Loops = a statement that will execute
# its block of code as long as its condition is true
# infinite loop

name = ""
while len(name) == 0:
    print("Welcome to the game")
    print("Please enter your name")
    name = input("What is your name? ")
    if name.isnumeric():
        print("Your name is not valid, please try again.")
        name = input("What is your name? ")
    break

###################################################################
# nested loops = The inner loops will finish all of its iterations before
# finishing one iteration of the outer loop


rows = int(input("How many rows would you like? "))
columns = int(input("How many columns would you like? "))
symbol = input("Enter the symbol you would like to use :")

for i in range(rows):
    for j in range(columns):
        print(symbol, end=" ")
    print()


###################################################################
# Loop Control
# break = used to terminate the loop completely
# continue =  skips to the next iteration of the loop
# pass = does nothing, acts as a place holder


while True:
    name = input("What is your name? ")
    if name != "":
        break

phone_number = "083-703-9797"
for i in phone_number:
    if i == "-" :
        continue
    else:
        print(i, end=" ")

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i, end=" ")


###################################################################

#Learning if statements

# This program checks if the user is an adult or a minor based on their age input.
# It uses an if statement to compare the age against 18 and prints the appropriate message.
# You can test this code by running it and entering different ages to see the output.
# Example inputs and outputs:
# Input: 20 -> Output: You are an adult.
# Input: 16 -> Output: You are a minor.

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
#if statements using bools
is_raining = True
if is_raining:
    print("Don't forget to take an umbrella!")
else:
    print("It's a sunny day, enjoy!")

# Nested if statements
number = int(input("Enter a number: "))
if number > 0:
    if number % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is not positive.")    

# Using elif for multiple conditions
score = int(input("Enter your score (0-100): "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")   
# Combining conditions with logical operators
temperature = int(input("Enter the temperature in Celsius: "))
if temperature > 30 and temperature <= 40:
    print("It's a hot day.")
elif temperature > 20 and temperature <= 30:
    print("It's a warm day.")
elif temperature > 10 and temperature <= 20:
    print("It's a cool day.")
else:
    print("It's a cold day.")   

# Using the not operator
is_weekend = False
if not is_weekend:  
    print("It's a weekday, time to work!")
else:
    print("It's the weekend, time to relax!")

# Checking membership with 'in' and 'not in'
fruits = ["apple", "banana", "cherry"]
favorite_fruit = input("Enter your favorite fruit: ").lower()
if favorite_fruit in fruits:
    print(f"{favorite_fruit.capitalize()} is a great choice!")
else:
    print(f"{favorite_fruit.capitalize()} is not in the list of available fruits.") 
if favorite_fruit not in fruits:
    print(f"{favorite_fruit.capitalize()} is not in the list of available fruits.") 
else:
    print(f"{favorite_fruit.capitalize()} is a great choice!")      

# Using if statements with strings
username = input("Enter your username: ")
if username == "admin":
    print("Welcome, admin!")        
else:
    print("Welcome, user!")
# Case insensitive check
if username.lower() == "admin":
    print("Welcome, admin!")        
else:
    print("Welcome, user!")

# Using if statements with lists
colors = ["red", "blue", "green"]
favorite_color = input("Enter your favorite color: ").lower()
if favorite_color in colors:
    print(f"{favorite_color.capitalize()} is a beautiful color!")
else:
    print(f"{favorite_color.capitalize()} is not in the list of available colors.")
 

# Using if statements with dictionaries
user_info = {"name": "Alice", "age": 30, "city": "New York"}
key_to_check = input("Enter the key you want to check (name, age, city): ").lower()
if key_to_check in user_info:
    print(f"The value for '{key_to_check}' is: {user_info[key_to_check]}")
else:
    print(f"'{key_to_check}' is not a valid key in the user info dictionary.")


# Using if statements with functions
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
number = int(input("Enter a number to check if it's even or odd: "))
result = check_even_odd(number)
print(f"The number {number} is {result}.")  


# Using if statements with lists and loops
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print("Even numbers in the list:", even_numbers)      


# Using if statements with list comprehensions
squared_even_numbers = [num**2 for num in numbers if num % 2 == 0]
print("Squared even numbers:", squared_even_numbers)


# Using if statements with try-except for error handling
user_input = input("Enter a number to divide 100 by: ")
try:
    divisor = float(user_input)
    if divisor == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = 100 / divisor
        print(f"100 divided by {divisor} is {result}.")
except ValueError:
    print("Error: Please enter a valid number.")    


# Using if statements with file operations
file_name = input("Enter the name of the file to check (e.g., test.txt): ")
try:
    with open(file_name, 'r') as file:
        content = file.read()
        if content:
            print(f"The file '{file_name}' is not empty.")
        else:
            print(f"The file '{file_name}' is empty.")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")

    
# Using if statements with classes and objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False        
person_name = input("Enter the person's name: ")
person_age = int(input("Enter the person's age: "))
person = Person(person_name, person_age)
if person.is_adult():
    print(f"{person.name} is an adult.")
else:
    print(f"{person.name} is a minor.")

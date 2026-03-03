#Logical operators in Python
# Demonstrating the use of logical operators: and, or, not, in, not in

# Using the 'and' operator
score = int(input("Enter your score (0-100): "))
if score >= 50 and score <= 60:
    print("The score is between 50 and 60.")
elif score > 60 and score <= 70:
    print("The score is between 61 and 70.")
elif score > 70 and score <= 80:
    print("The score is between 71 and 80.")
elif score > 80 and score <= 100:
    print("The score is between 81 and 100.")
elif score < 50:
    print("You did not pass the exam.")


# Using the 'or' operator
weather = input("Enter the weather (rainy/sunny/cloudy): ").lower()
if weather == "rainy" or weather == "cloudy":
    print("It's a gloomy day, stay indoors!")
elif weather == "sunny":
    print("It's a sunny day, enjoy!")

#Uisng the not operator
is_weekend = False
if not is_weekend:
    print("It's a weekday, time to work!")
elif is_weekend:
    print("It's the weekend, time to relax!")

#Using the 'in' operator
fruits = ["apple", "banana", "cherry"]
favorite_fruit = input("Enter your favorite fruit: ").lower()
if favorite_fruit in fruits:
    print(f"{favorite_fruit.capitalize()} is a great choice!")
elif favorite_fruit not in fruits:
    print(f"{favorite_fruit.capitalize()} is not in the list of available fruits.")

# Using the 'not in' operator
fruits = ["apple", "banana", "cherry"]
favorite_fruit = input("Enter your favorite fruit: ").lower()
if favorite_fruit not in fruits:
    print(f"{favorite_fruit.capitalize()} is not in the list of available fruits.")
elif favorite_fruit in fruits:
    print(f"{favorite_fruit.capitalize()} is a great choice!")
    

#User Input 

name:str  = input("WHat is your name: ")

print(f"Your name is {name}")

age: int = int(input("How old are you: "))
print(f"You are {age} years old")


print(f"You will be {age+1}years old next year")

sick: str =input("Are you sick: ")
is_sick = False

if sick == "yes":
    is_sick=True
    print("Oh no you are sick")
else:
    is_sick=False
    print("Yay you are not sick")


print(f"{str(is_sick)}")
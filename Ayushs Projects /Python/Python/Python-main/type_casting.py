#Type casting 
#Changing the type of varibales 

name = "Ayush"
age =21
gpa = 3.6
is_student = True



print(f"The type for {name} is {type(name)}")
print(f"The type for {age} is {type(age)}")
print(f"The type for {gpa} is {type(gpa)}")
print(f"The type for {is_student} is {type(is_student)}")

#Type cast function 
gpa = int(gpa)
age = float(age)
age3 = str(age)
is_student = str(is_student)

print(f"The type for {gpa} is {type(gpa)}")
print(f"The type for {age} is {type(age)}")
print(f"The type for {age3} is {type(age3)}")
print(f"The type for {is_student} is {type(is_student)}")

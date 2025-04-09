# Variable = A container for a value (string, integer, float, boolean)
#            A variable as if it was the value it contains

# This is my first Python program
print("I like pizza!")
print("It's really good!")

# Strings
first_name = "Ashlesh"
food = "Pizza"
email = "ashlesh@gmail.com"

print(first_name)

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")

#Integers
age = 25
quantity = 3
num_of_students = 30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

#Float
price = 10.99
gpa = 9.95
distance = 5.5

print(f"The price is {price}")
print(f"Your gpa is {gpa}")
print(f"You ran {distance}km")

#Boolean
is_student = True

if is_student:
    print("I am a student")
else:
    print("I am not a student")

print(f"Are you a student?: {is_student}")

for_sale = True

if for_sale:
    print("That item is for sale")
else:
    print("That item is not available")    

is_online = False

if is_online:
    print("You are online")
else:
    print("You are offline")
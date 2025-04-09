# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

name = input("What is your name?: ")
age = input("How old are you?: ")

age = int(age)    # or we can also use int(input("How old are you?: "))
age += 1

print(f"Hello {name}!")
print("Happy Birthday!")
print(f"You are {age} years old")

# Exercise 1 Rectangle Area Calc

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

Area = length * width

print(f"The area of the rectangle is {Area}cm^2")

# Exercise 2 Shopping Cart Program 

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"You have bought {quantity} * {item}/s")
print(f"Your total is {total}")
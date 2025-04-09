# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
# Print or assign one of two values based on a condition

# To check whether a number is Positive or Negative
num = int (input("Enter a number: "))
print("Positive" if num > 0 else "Negative")

# To check whether a number is Even or Odd
num1 = int(input("Enter a number: "))
print("Even" if num1 % 2 == 0 else "Odd")

# To check greater between two numbers
a = int(input("Assign a number to a: "))
b = int(input("Assign a number to b: "))
print("a" if a > b else "b")

# To check smallest between two numbers
a = int(input("Assign a number to a: "))
b = int(input("Assign a number to b: "))
print("a" if a < b else "b")

# To check whether a person is Adult or a child
age = int(input("Enter a age: "))
print("Adult" if age >= 18 else "Child")

# To Display the type of weather depending on the temperature
temperature = float(input("Enter the temperature: "))
print("Hot" if temperature > 20 else "Cold")

# To check whether a person is admin or not 
user_role = input("Enter the user role: ")
print("Full Access" if user_role == "admin" else "Limited Access")
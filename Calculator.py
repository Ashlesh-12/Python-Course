# Python Calculator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
symbol = input("Enter the operation to perform: ")

if symbol == "+":
    print(f"The sum of {num1} and {num2} is {num1 + num2}")
elif symbol == "-":
    print(f"The difference of {num1} and {num2} is {num1 - num2}")
elif symbol == "*":
    print(f"The product of {num1} and {num2} is {num1 * num2}")
elif symbol == "/":
    print(f"The quotient of {num1} and {num2} is {round((num1 / num2), 2)}")
elif symbol == "%":
    print(f"The remainder of {num1} and {num2} is {round((num1 % num2, 2))}")
else:
    print(f"Wrong operation given! ({symbol})")

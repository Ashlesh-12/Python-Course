# Weight Converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or P): ")

if unit == "K":
    print(f"Your weight in pounds is: {round((weight * 2.205), 1)}Lbs.")
elif unit == "P":
    print(f"Your weight in Kilograms is: {round((weight/2.205), 1)}Kgs.")
else:
    print(f"{unit} was not valid")
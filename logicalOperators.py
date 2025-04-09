# logical operators = evaluate multiple conditions (or, and, not)
# or = at least one condition must be True
# and = both conditions must be True
# not = inverts the condition (not False, not True)

temp = float(input("Enter the temperature: "))

is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")
    
temp1 = float(input("Enter the temperature: "))

is_sunny = False

if temp1 >= 28 and is_sunny:
    print("It is Hot outside")
    print("It is Sunny")
elif temp1 <= 0 and is_sunny:
    print("It is Cold outside")
    print("It is Sunny")
elif temp1 < 28 and temp1 > 0 and is_sunny:
    print("It is Warm outside")
    print("It is Sunny")
elif temp1 >= 28 and not is_sunny:
    print("It is Hot outside")
    print("It is Cloudy")
elif temp1 <= 0 and not is_sunny:
    print("It is Cold outside")
    print("It is Cloudy")
elif temp1 < 28 and temp1 > 0 and not is_sunny:
    print("It is Warm outside")
    print("It is Cloudy")
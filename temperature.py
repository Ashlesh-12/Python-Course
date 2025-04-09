# Temperature Converter

# To convert Celsius to Fahrenheit: F = C * 9 / 5 + 32
# To convert Fahrenheit to Celsius: C = (F - 32) * 5 / 9 
# To convert Celsius to Kelvin: K = C + 273.15
# To convert Kelvin to Celsius: C = K - 273.15
# To convert Fahrenheit to Kelvin: K = (F - 32) * 5 / 9 + 273.15
# To convert Kelvin to Fahrenheit: F = (K - 273.15) * 9 / 5 + 32

temperature = float(input("Enter the temperature: "))
initial_unit = input("Enter the initial unit (C/F/K): ")
converted_unit = input("Enter the unit to which the initial unit has to be converted (C/F/K): ")

if initial_unit == "C":
    if converted_unit == "F":
        print(f"The temperature ({temperature}C) in Farenheight scale is: {round(((temperature * (9 / 5)) + 32), 2)}F")
    elif converted_unit == "K":
        print(f"The temperature ({temperature}C) in Kelvin scale is: {round((temperature + 273.15), 2)}K")
        
elif initial_unit == "F":
    if converted_unit == "C":
        print(f"The temperature ({temperature}F) in Celsius scale is: {round(((temperature - 32) * (5 / 9)), 2)}C")
    elif converted_unit == "K":
        print(f"The temperature ({temperature}F) in Kelvin scale is: {round(((temperature - 32) * (5 / 9) + 273.15), 2)}K")
        
elif initial_unit == "K":
    if converted_unit == "C":
        print(f"The temperature ({temperature}K) in Celsius scale is: {round((temperature - 273.15), 2)}C")
    elif converted_unit == "F":
        print(f"The temperature ({temperature}K) in Celsius scale is: {round(((temperature - 273.15) * (9 / 5) + 32), 2)}F")
        
else:
    print("Invalid unit! Please re-enter the unit (C/F/K)")
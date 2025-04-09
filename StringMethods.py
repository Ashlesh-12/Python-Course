# #length of a string
# name = input("Enter your full name: ")
# print(len(name))

# # find method
# name1 = input("Enter your name: ")
# print(name1.find("l"))

# # find method (reverse or last occurance)
# name2 = input("Enter your name: ")
# print(name2.rfind("s"))

# # Capatilize
# name3 = input("Enter your name: ")
# print(name3.capitalize())

# # Uppercase
# name4 = input("Enter your name: ")
# print(name4.upper())

# # Lowercase
# name5 = input("Enter your name: ")
# print(name5.lower())

# # isdigit
# name6 = input("Enter your name: ")
# print(name6.isdigit())

# #isalpha
# name7 = input("Enter your name: ")
# print(name7.isalpha())

# #Count
# phone_number = input("Enter your phone number: ")
# print(phone_number.count("7"))

# #replace
# phone_number = input("Enter your phone number: ")
# print(phone_number.replace("-", " "))

# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username nust not contain digits

username = input("Enter your username: ")
if len(username) >12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't have spaces")
elif not username.isalpha():
    print("Your username can't have digits")
else:
    print(f"Welcome {username}")
# Typecasting = The process of converting a variable from one data type to another
#               str(), int(), float(), bool()

name1 = "S Ashlesh Pai"
age = 19
gpa = 9.95
is_student = True

print(type(name1))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)
print(gpa)

age = float(age)
print(age)

age = str(age)
print(age)

print(type(age))

age += "1"
print(age)

name1 = bool(name1)
print(name1)

name2 = ""
name2 = bool(name2)
print(name2)
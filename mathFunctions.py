import math

x = 3.14
y = 4
z = 5

result = round(x)
print(result)

result1 = abs(y)
print(result1)

result2 = pow(y,z)
print(result2)

result3 = max(x,y,z)
print(result3)

result4 = min(x,y,z)
print(result4)

print(math.pi)
print(math.e)
print(math.sqrt(y))
print(math.ceil(x))
print(math.floor(x))

# To find Circumfurence of a circle
r = float(input("Enter the radius of the circle: "))
answer = 2*math.pi*r
print(f"The circumference of the circle is: {round(answer, 2)}cm")

# To find the Area of a circle
r1 = float(input("Enter the radius of the circle: "))
area = math.pi*pow(r1,2)
print(f"The Area of the circle is: {round(area, 2)}cm^2")

# To find the hypotenuse of a right angled triangle
a = float(input("Enter the value of side a: "))
b = float(input("Enter the value of side b: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"The Hypotenuse of the right angled triangle is: {round(c, 2)}cm")

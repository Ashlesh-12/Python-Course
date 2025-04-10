# collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# LIST

fruits = ["apple", "orange", "banana", "coconut"]
# print(fruits)
# print(fruits[1])
# print(fruits[::-1])
# print(len(fruits))
# print("apple" in fruits)

# for fruit in fruits:
#     print(fruit)
    
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("apple"))
print(fruits.count("apple"))

# print(fruits)

# SET

fruits1 = {"apple", "orange", "banana", "coconut"}
# fruits1.add("pineapple")
# fruits1.remove("pineapple")
# fruits1.pop()
print(fruits1)

# TUPLE

fruits2 = ("apple", "orange", "banana", "coconut", "apple")
print(fruits2.index("apple"))
print(fruits2.count("apple"))

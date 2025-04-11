# dictionary = a collection of {key:value} pairs
# ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

print(capitals.get("India"))

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist")
    
capitals.update({"Germany": "Berlin"}) # we can also update a key and a value which is already existing
print(capitals)
print(capitals.values())
print(capitals.keys())

capitals.pop("China")
capitals.popitem()
print(capitals)


for keys in capitals.keys():
    print(keys)

for values in capitals.values():
    print(values)
    
print(capitals.items())

for key, value in capitals.items():
    print(f"{key}: {value}")

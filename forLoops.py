# for loops = execute a bloack of code a fixed number of times.
# You can iterate over a range, string,sequence, etc.

for i in reversed(range(1, 11)):
    print(i , end=" ")
print("\nHappy New Year!")

# Step Count in range
for j in range(1, 11, 2):
    print(j, end = " ")
    
# Iterating over a string
credit_number = "1234-5678-9012-3456"
for count in credit_number:
    print(count , end = " ")
    
# Continue   
for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)
        
# Break        
for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)

myArray = ["R","K","J","M","B"]

# access array
for x in myArray:
    print(x)

# array length
print(len(myArray)) #5

# add elements
myArray.append("L")

print(myArray)  #['R', 'K', 'J', 'M', 'B', 'L']

# remove elements
myArray.remove("B")

print(myArray) #['R', 'K', 'J', 'M', 'L']

myArray.pop(4)  # with index number

print(myArray) #['R', 'K', 'J', 'M']
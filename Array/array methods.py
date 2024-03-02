
myArray = ["R","K","J","M","B"]
myNewArray={"p","o","Q"}
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



myArray.reverse()

print(myArray)  #['B', 'M', 'J', 'K', 'R']



myArray.sort(reverse=True)

print(myArray) #['R', 'M', 'K', 'J', 'B']



def myfunc(take):
  return take["age"]


names = [{"name":"R", "age":"2022"},{"name":"Md", "age":"2023"},{"name":"K","age":"202024"}]

names.sort(key=myfunc, reverse=True)
print(names)



myArray.extend(myNewArray)

print(myArray) #['R', 'K', 'J', 'M', 'B', 'p', 'o', 'Q']
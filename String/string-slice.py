
name ="what is my name?"


# check string 
print("is" in name)     
print("jaman" in name)
print("jaman" not in name) #True



# length of string 

print(len(name))

# access each character
for x in name:
    print(x)


# slicing strings
    
s="understanding-slicing"

print(s[2])   # d

print(s[2:])  # derstanding-slicing
print(s[:5])  # under
print(s[2:5]) # der -> first 2 will work than 5 


print(s[:-5])   #understanding-sl

print(s[-2:])   # ng

print(s[-5:-2]) #ici


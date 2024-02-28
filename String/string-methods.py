
text = " learning, STRING, Method"

print(text.upper())

print(text.lower())

print(text.capitalize())

print(text.strip())  #learning, STRING, Method  -remove whitespace

print(text.replace("l", "b"))  # bearning, STRING, Method

print(text.split(","))  # [' learning', ' STRING', ' Method']

print(text.title()) #Learning, String, Method

print(text.find("STRING")) 

print(text.find("jaman")) # -1 if not found 

print(text.index("STRING"))

print(text.index("JAMAN")) # ValueError: substring not found

print(">".join(text)) # >l>e>a>r>n>i>n>g>,> >S>T>R>I>N>G>,> >M>e>t>h>o>d

print(text.count) 


num="3"
print(num.zfill(5))

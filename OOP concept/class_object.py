

# declared class name jaman
class jaman:

# the __init__() function
    
    def __init__(self, name, age, address ):
        self.name = name
        self.age = age
        self.address = address
     
# calling the class name jaman and pass the arguments

person = jaman("jaman", 24, "Germany")

print(person.name, person.age, person.address)





# The __str__() Function

class kamrul:

    def __init__(self,name,age,country):
        self.name = name
        self.age = age
        self.country = country

        
    def myfunc(self):
        
        print("My name is " + self.name)

    def __str__(self):
           
           return f"{self.name} {self.country} ({self.age})" 

person = kamrul("jaman",24, "germany")

# calling by class arguments
print(person.name,person.age,person.country)

#calling by class
print(person)

# calling by class function
person.myfunc()
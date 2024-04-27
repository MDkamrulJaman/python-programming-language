import os

print("Working with file handling" + "\n")

file_name = "Programing.txt"

#create the file

file = open(file_name, 'w')
file.writelines([" ", "You are welcome to the world\n"])
file.write("I am Md Kamrul jaman rabbi.")
file.write("I am 24 years old")

#read the file
file = open(file_name, "r")

content_file = file.read()
print(content_file)

file.close()



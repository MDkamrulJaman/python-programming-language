import os

print("append the files contents")

#create file1
file_name1 = "file1.txt"

file1 = open(file_name1,'w')

file1.write("I am file_1")

file1 = open(file_name1,'r')

file1_content = file1.read()
print(file1_content)

file1.close()

#create file2
file_name2 = "file2.txt"

file2 = open(file_name2,'w')
file2.write("I am file_2")

file2 = open(file_name2,'r')

file2_content = file2.read()

print(file2_content)


file2.close()

# crate main file which contain both files content
file_name = "file.txt"

file = open(file_name,'a')

file_content = file1_content + file2_content

file.write(file_content)

file = open(file_name,'r')
all_file_contents = file.read()
print(all_file_contents)

file.close()



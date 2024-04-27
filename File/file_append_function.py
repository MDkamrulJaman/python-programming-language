import os

def read_file_content(filename):
    file = open(filename, 'r')
    content = file.read()
    file.close()
    return content

def append_files_content(file_names, new_file_name):
    new_file = open(new_file_name, 'a')
    for file_name in file_names:
        file_content = read_file_content(file_name)
        new_file.write(file_content)
    new_file.close()



def create_file(filename, content):
    file = open(filename, 'w')
    file.write(content)
    file.close()

def read_from_file(filename):
    return read_file_content(filename)


def main():
    print("Append the files contents")

    #file1 
    file_content1 = input("Enter content for file 1: ")
    file_name1 = input("Enter filename for file 1: ") + ".txt"
    create_file(file_name1, file_content1)

    # file2 
    file_content2 = input("Enter content for file 2: ")
    file_name2 = input("Enter filename for file 2: ") + ".txt"
    create_file(file_name2, file_content2)

    # Get all file names
    file_names = [file_name1, file_name2]

    # Take new file name input
    new_file_name = input("Enter filename for the new file to append contents: ") + ".txt"

    # Append contents of file1 and file2 to new file
    append_files_content(file_names, new_file_name)

    # Read content of new file
    all_file_contents = read_from_file(new_file_name)
    print("Contents of", new_file_name, ":")
    print(all_file_contents)

if __name__ == "__main__":
    main()
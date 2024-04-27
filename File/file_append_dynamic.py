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
    print("append the files contents")

    file_names = []  

    while True:
        file_content = input("Enter content for the file:")
        if file_content.lower() == 'done':
            break 

        file_name = input("Enter filename for the file: ") + ".txt"
        create_file(file_name, file_content)
        file_names.append(file_name)  # Add the filename to the list

    if len(file_names) == 0:
        print("No files to append. Exiting...")
        return

    # Take new file name input
    new_file_name = input("Enter filename for the new file to append contents: ") + ".txt"

    # Append contents of all files to new file
    append_files_content(file_names, new_file_name)

    # Read content of new file
    all_file_contents = read_from_file(new_file_name)
    print("Contents of", new_file_name, ":")
    print(all_file_contents)

if __name__ == "__main__":
    main()

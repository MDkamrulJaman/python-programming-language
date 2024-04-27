class FileManager:
    def __init__(self):
        self.file_names = []

    def read_file_content(self, filename):
        """Reads and returns the content of a file."""
        with open(filename, 'r') as file:
            content = file.read()
        return content

    def append_files_content(self, new_file_name):
        """Appends the content of all registered files into a new file."""
        with open(new_file_name, 'a') as new_file:
            for file_name in self.file_names:
                file_content = self.read_file_content(file_name)
                new_file.write(file_content)

    def create_file(self, filename, content):
        """Creates a file with the specified content."""
        with open(filename, 'w') as file:
            file.write(content)
        self.file_names.append(filename)  # Register the file name after creating it

    def read_from_file(self, filename):
        """Reads and returns the content from a file."""
        return self.read_file_content(filename)

    def main(self):
        """The main interactive loop to handle file creation and content appending."""
        print("Append the files contents")

        while True:
            file_content = input("Enter content for the file (or type 'done' to finish): ")
            if file_content.lower() == 'done':
                break

            file_name = input("Enter filename for the file: ") + ".txt"
            self.create_file(file_name, file_content)

        if not self.file_names:
            print("No files to append. Exiting...")
            return

        new_file_name = input("Enter filename for the new file to append contents: ") + ".txt"
        self.append_files_content(new_file_name)

        all_file_contents = self.read_from_file(new_file_name)
        print(f"Contents of {new_file_name}:")
        print(all_file_contents)

if __name__ == "__main__":
    file_manager = FileManager()
    file_manager.main()

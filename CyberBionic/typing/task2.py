from typing import List, Optional


class Directory:
    """Init class of directory files"""

    def __init__(self, name: str, root: Optional["Directory"]) -> None:
        self.name = name
        self.root = root
        self.files: List["File"] = []
        self.sub_directories: List["Directory"] = []

    def add_sub_directory(self, sub_directory: Optional["Directory"]) -> None:
        """Args: sub_directory (Optional[&quot;Directory&quot;]): adding subdirectory"""

        if sub_directory not in self.sub_directories:
            self.sub_directories.append(sub_directory)

    def remove_sub_directory(self, sub_directory: Optional["Directory"]) -> None:
        """Args: sub_directory (Optional[&quot;Directory&quot;]): removing subdirectory"""

        if sub_directory in self.sub_directories:
            self.sub_directories.remove(sub_directory)

    def add_file(self, file: Optional["File"]) -> None:
        """Args: file (Optional[&quot;File&quot;]): adding file"""

        if file not in self.files:
            self.files.append(file)
        else:
            print(f"File '{file.name}' already exists in directory '{self.name}'.")

    def remove_file(self, file: Optional["File"]) -> None:
        """Args: file (Optional[&quot;File&quot;]): removing file"""

        if file in self.files:
            self.files.remove(file)
        else:
            print(f"File '{file.name}' not found in directory '{self.name}'.")

    def __str__(self) -> str:
        files = "".join(file.name for file in self.files)
        return f"Directory({self.name}=[{files}])"


class File:
    """Init class for a file"""

    def __init__(self, name: str, directory: Optional["Directory"]) -> None:
        self.name = name
        self.directory = directory

    def __str__(self):
        print(f"File: {self.name}")


directory = Directory("Windows", "root") #Create a directory

sub_directory = Directory("Program files", "root") #Create a sub_directory

file_name1 = File("test1.txt", sub_directory) #Create file1
file_name2 = File("test2.txt", sub_directory) #Create file2

directory.add_file(file_name1) #Adding file to directory
directory.add_sub_directory(sub_directory) #Adding sub_directory
sub_directory.add_file(file_name2) #Adding file to sub_directory

print(directory)
print(sub_directory)

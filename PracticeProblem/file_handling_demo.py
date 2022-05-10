
def file_operation_write():
    """
    function for write into file
    :return: the desired output
    """
    # Python code to write a file
    file = open('file.txt', 'w')  # 'w' will override the existing text available in file
    file.write("This is the write command")
    file.write("It allows us to write in a particular file")
    file.close()


def file_operation_read():
    """
    function for read the file
    :return: all elements of that file
    """
    # Python code to read a file
    file = open("file.txt", "r")
    print(file.read())
    file.close()


def file_operation_append():
    """
    function for appending
    :return: write the text in file in a new line
    """
    file1 = open("file.txt", "a")  # 'a' to write the text in file and didn't override the existing text
    # Writing to file
    file1.write("\nWriting to file")
    # Closing file
    file1.close()


if __name__ == "__main__":
    file_operation_write()
    file_operation_read()
    file_operation_append()
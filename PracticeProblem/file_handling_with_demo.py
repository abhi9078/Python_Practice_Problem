
def file_operation():
    """
    function for file operation
    :return: desire output
    """
    with open("text.txt", "w") as f:
        f.write("Hello World!!!")
        f.write("\nHello, I am Abhilash Meher")


def file_read():
    with open("text.txt", "r") as file:
        data = file.readlines()
        for line in data:
            word = line.split()
            print(word)


if __name__ == "__main__":
    file_operation()
    file_read()

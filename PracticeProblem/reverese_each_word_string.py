
def reverse_word(input_string):
    """
    function will return reverse word of each string
    :param input_string:getting a string input from user
    :return:reverse of each string
    """
    new_list = []

    for i in range(len(input_string)):
        if input_string[i] != " ":
            new_list.append(input_string[i])

        else:
            while len(new_list) > 0:
                print(new_list[-1], end="")
                new_list.pop()
            print(end=" ")

    while len(new_list) > 0:
        print(new_list[-1], end="")
        new_list.pop()


if __name__ == "__main__":
    string_in = "hello world"
    reverse_word(string_in)

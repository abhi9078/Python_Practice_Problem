
def frequency_of_character(input_str):
    """
    function for counting character in string
    :param input_str: take input of string
    :return: frequency of character
    """
    d1 = {}

    for i in input_str:
        if i in d1:
            d1[i] = d1[i] + 1
        else:
            d1[i] = 1
    return d1


if __name__ == "__main__":
    str1 = input("Please enter a string")
    output = frequency_of_character(str1)
    print(output)

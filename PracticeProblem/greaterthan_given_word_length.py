def my_func(str_input, k):
    """
    function for getting word more than given length
    :param str_input: input string by user
    :param k: given word length
    :return: words that are higher length
    """
    my_list = []
    my_list = str_input.split(" ")
    for i in my_list:
        if len(i) > k:
            print(i)


if __name__ == "__main__":
    input_str = input("Enter a sentence ")
    k_len = int(input("enter length "))
    my_func(input_str, k_len)

def sum_of_positive(list_input):
    """
    function for adding positive number in list
    :param list_input: list of input
    :return: sum of positive number
    """
    add_positive = 0
    for i in list_input:
        if i > 0:
            add_positive = add_positive+i

    return add_positive


def sum_of_negative(list_in):
    """
    function for adding negative number
    :param list_in: list of input
    :return: sum of negative number
    """
    add_negative = 0
    for j in list_in:
        if j < 0:
            add_negative = add_negative + j
    return add_negative


if __name__ == "__main__":
    lt = [1, 6, -9, -3, 5]
    negative_sum = sum_of_negative(lt)
    positive_sum = sum_of_positive(lt)
    print("Sum of all negative number in the list is: ", negative_sum)
    print("Sum of all positive number in the list is: ", positive_sum)

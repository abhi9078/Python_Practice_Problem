def sum_of_array(f_list, s_list):
    """
    function for calculating sum of two different list
    :param f_list: first list from user
    :param s_list: second list from user
    :return: sum of each element at position
    """
    sum_list = []
    for i in range(0, len(f_list)):
        list_sum = f_list[i]+s_list[i]
        sum_list.append(list_sum)

    return sum_list


if __name__ == "__main__":
    first = [1, 2, 3, 4]
    second = [5, 6, 7, 8]
    output = sum_of_array(first, second)
    print("The sum of two different array of same length is: ", output)

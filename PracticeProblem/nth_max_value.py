
def maximum(number_list):
    """
    function for getting nth max element from list
    :param number_list: to get a list
    :return: nth max value
    """
    max_list = number_list[0]

    for i in number_list:
        if i > max_list:
            max_list = i

    return max_list


if __name__ == "__main__":
    user_list = [10, 2, 6, 20, 8, 9]
    nth_max = maximum(user_list)
    print("The nth max value is: ", nth_max)
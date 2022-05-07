def list_demo(list_of_num):
    """
    Function to perform some list operation
    :param list_of_num: accept a list of integer
    :return:some performed operation
    """
    print("the first element is: ", list_of_num[0])
    print("the length of list is: ", len(list_of_num))
    print("the last element is: ", list_of_num[-1])
    print("Reverse order is: ", list_of_num[::-1])


if __name__ == "__main__":
    f_list = [2, 4, 8, 9, 0, 4, 88]
    list_demo(f_list)

def bubble_sort(num_list):
    """
    function to perform bubble sort
    :param num_list: list of elements
    :return: sorted list
    """
    for i in range(len(num_list)-1, 0, -1):
        for j in range(i):
            if num_list[j] > num_list[j+1]:
                temp = num_list[j]
                num_list[j] = num_list[j+1]
                num_list[j+1] = temp


if __name__ == "__main__":
    arr = [3, 2, 9, 6, 1, 4]
    bubble_sort(arr)
    print(arr)
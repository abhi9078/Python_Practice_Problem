def insertion_sort(arr_list):
    """
    function for perform insertion sort
    :param arr_list: list of elements
    :return: sorted array
    """
    for i in range(1, len(arr_list)):
        j = i
        while arr_list[j - 1] > arr_list[j] and j > 0:
            arr_list[j - 1], arr_list[j] = arr_list[j], arr_list[j - 1]
            j -= 1


if __name__ == "__main__":
    arr = [2, 5, 1, 3, 10, 4]
    insertion_sort(arr)
    print(arr)

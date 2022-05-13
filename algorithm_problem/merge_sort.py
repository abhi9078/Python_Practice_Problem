def merge_sort(arr_list):
    """
    function for performing merge sort
    :param arr_list: list of elements
    :return: sorted list
    """
    if len(arr_list) > 1:
        left_arr = arr_list[:len(arr_list)//2]
        right_arr = arr_list[len(arr_list)//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = 0
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr_list[k] = left_arr[i]
                i += 1
                k += 1
            else:
                arr_list[k] = right_arr[j]
                j += 1
                k += 1

        while i < len(left_arr):
            arr_list[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr_list[k] = right_arr[j]
            j += 1
            k += 1


if __name__ == "__main__":
    arr = [3, 5, 1, 8, 4, 9, 2]
    merge_sort(arr)
    print(arr)



def find_triplets(arr, n):
    """
    Function will find all possible triplets
    :param arr: for declaring an array of elements
    :param n: array length
    :return: all possible triplets
    """
    for i in range(0, n-2):
        for j in range(0, n-1):
            for k in range(0, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    print(arr[i], arr[j], arr[k])


if __name__ == "__main__":
    arr_items = [1, 2, -1, 3, -2]
    length = len(arr_items)
    print("All possible triplets are: ")
    find_triplets(arr_items, length)








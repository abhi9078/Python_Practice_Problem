def sort(lt):
    """
    function for sorting a list
    :param lt: input list
    :return: sorted lst
    """
    for i in range(len(lt)):
        for j in range(i+1, len(lt)):
            if lt[i] > lt[j]:
                lt[i], lt[j] = lt[j], lt[i]

    return lt


def index_element(list_in, n):
    """
    function for getting index of new element and insert it to sorted list
    :param list_in: input list
    :param n: new element
    :return: index of new element
    """
    list_in.append(n)
    s_list = sort(list_in)

    for i in range(len(s_list)):
        if s_list[i] == n:
            return f"Index of the inserted element is: {i}"


if __name__ == "__main__":
    input_list = [1, 4, 6, 7, 9]
    new_item = 5
    print(index_element(input_list, new_item))

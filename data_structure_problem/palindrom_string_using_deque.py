from collections import deque


def pal_checker(str_in):
    """
    function for check palindrome string using deque
    :param str_in: string input from user
    :return: palindrome string
    """
    char_deque = deque()

    for ch in str_in:
        char_deque.append(ch)

    still_equal = True

    while len(char_deque) > 1 and still_equal:
        first = char_deque.popleft()
        last = char_deque.pop()
        if first != last:
            still_equal = False

    return still_equal


if __name__ == "__main__":
    str_input = input("enter a string")
    output = pal_checker(str_input)
    print("Given string is: ", output)

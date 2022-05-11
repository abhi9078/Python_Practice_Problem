
def equality_of_lines(x1, y1, x2, y2):
    """
    function for check equality of lines
   :param x1:first coordinate of first line
    :param y1:second coordinate of first line
    :param x2:first coordinate of second line
    :param y2:first coordinate of second line
    :return: equality of lines
    """
    if x1 == x2:
        if y1 == y2:
            return "Lines are Equals"
        else:
            return "Lines are not equal"
    else:
        len1 = y1-x1
        len2 = y2-x2
        if len1 == len2:
            return "Lines are Equals"
        else:
            return "Lines are not equal"


if __name__ == "__main__":
    output = equality_of_lines(3, 5, 2, 4)
    print(output)
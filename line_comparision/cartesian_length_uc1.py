
def cartesian_length(x1, y1, x2, y2):
    """
    function for calculating cartesian length of two line
    :param x1:first coordinate of first line
    :param y1:second coordinate of first line
    :param x2:first coordinate of second line
    :param y2:first coordinate of second line
    :return:cartesian length
    """
    result = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    return result


if __name__ == "__main__":
    output = cartesian_length(2, 4, 6, 9)
    print("cartesian length is: ", output)


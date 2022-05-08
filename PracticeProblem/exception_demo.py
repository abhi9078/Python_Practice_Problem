
def fun(a):
    """
    function for exception handling
    :param a: will get a number
    :return: desire output
    """
    if a < 4:
        b = a / (a - 3)

    print("Value of b = ", b)


if __name__ == "__main__":
    try:
        fun(3)
    except ZeroDivisionError:
        print("ZeroDivisionError Occurred and Handled")

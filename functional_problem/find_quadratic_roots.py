import math


def find_quadratic_roots(a, b, c):
    """
    function for finding the quadratic roots
    :param a: first value
    :param b: second value
    :param c: third value
    :return: two roots of the equation
    """
    root = b*b - 4*a*c
    delta = math.sqrt(root)
    root1 = (-b + delta)/2*a
    root2 = (-b - delta)/2*a
    print("first roots of the equation is: ", root1)
    print("second roots of the equation is: ", root2)


if __name__ == "__main__":
    x = int(input("please enter x value: "))
    y = int(input("please enter y value: "))
    z = int(input("please enter z value: "))
    find_quadratic_roots(x, y, z)

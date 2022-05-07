import math


def euclidean_distance(x, y):
    """
    function to calculate euclidean distance from origin (0,0)
    :param x:first coordinate
    :param y:second coordinate
    :return:distance from origin
    """
    if x == 0 and y == 0:
        print("distance is zero")
    else:
        distance = math.sqrt(x**x + y**y)
        print("The distance is: ", distance)


if __name__ == "__main__":
    first = int(input("First coordinate value: "))
    second = int(input("second coordinate value: "))
    euclidean_distance(first, second)


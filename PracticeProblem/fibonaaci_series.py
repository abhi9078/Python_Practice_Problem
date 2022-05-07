def fibonacci_series(last_range):
    """
    Function is to Find the Sequence of Fibonacci series
    :param last_range: Last sequence number of fibonacci series
    :return: will return the fibonacci series up to a range
    """
    count = 0
    num1, num2 = 0, 1

    # Loop for finding series 
    while count < last_range:
        print(num1)
        nth = num1 + num2
        num1 = num2
        num2 = nth
        count += 1


if __name__ == "__main__":
    last_num = int(input("Please enter last range"))
    if last_num < 0:
        print("Please enter a positive number")
    else:
        fibonacci_series(last_num)



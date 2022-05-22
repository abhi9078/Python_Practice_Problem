def perfect_number(num):
    """
    Function for check number is perfect or not
    :param num: given number
    :return: true or false
    """
    sum_of_num = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_num = sum_of_num+i

    if sum_of_num == num:
        return "Number is perfect number"
    else:
        return "Number is not perfect number"


if __name__ == "__main__":
    number = 6
    output = perfect_number(number)
    print(output)

import random


def emp_present_absent():
    """
    function for checking employee present or not
    :return: desire output
    """
    check = random.randint(0, 1)
    if check == 0:
        return "Employee is present"
    else:
        return "Employee is Absent"


if __name__ == "__main__":
    output = emp_present_absent()
    print(output)

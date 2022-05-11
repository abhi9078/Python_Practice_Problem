import random


def daily_wage():
    """
    function for calculating employee daily wage
    :return: daily wage if employee is present
    """
    wage_per_hour = 20
    working_hour = 8

    check = random.randint(0, 1)
    if check == 0:
        emp_wage = wage_per_hour*working_hour
        return emp_wage
    else:
        emp_wage = 0
        return emp_wage


if __name__ == "__main__":
    output = daily_wage()
    print("Total employee wage of the day is: ", output)

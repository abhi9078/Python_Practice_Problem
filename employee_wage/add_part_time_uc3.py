import random


def daily_wage():
    """
    function for calculating employee daily wage
    :return: daily wage if employee is present
    """
    wage_per_hour = 20
    full_working_hour = 8
    part_time_hour = 4

    check = random.randint(0, 2)
    if check == 0:
        print("Employee is present and doing full time")
        emp_wage = wage_per_hour*full_working_hour
        return emp_wage
    elif check == 1:
        print("Employee is present and doing part time")
        emp_wage = wage_per_hour*part_time_hour
        return emp_wage
    else:
        print("Employee is Absent")
        emp_wage = 0
        return emp_wage


if __name__ == "__main__":
    output = daily_wage()
    print("Total employee wage of the day is: ", output)

import random


def monthly_wage():
    """
    function for calculating employee monthly wage
    :return: monthly wage
    """
    wage_per_hour = 20
    full_working_hour = 8
    part_time_hour = 4
    total_working_days = 20
    total_working_hour = 100
    number_of_working_days = 0
    total_wage = 0
    emp_hours = 0

    while number_of_working_days < total_working_days and emp_hours <= total_working_hour:
        number_of_working_days += 1
        check = random.randint(0, 2)
        if check == 0:
            print("Employee is present and doing full time")
            emp_wage = wage_per_hour * full_working_hour
            total_wage = total_wage+emp_wage
            emp_hours = emp_hours + 8

        elif check == 1:
            print("Employee is present and doing part time")
            emp_wage = wage_per_hour * part_time_hour
            total_wage = total_wage + emp_wage
            emp_hours = emp_hours + 4
        else:
            print("Employee is Absent")
            emp_wage = 0
            total_wage = total_wage + emp_wage
            emp_hours = emp_hours + 0
    return total_wage


if __name__ == "__main__":
    output = monthly_wage()
    print("Total employee wage of the month is : ", output)

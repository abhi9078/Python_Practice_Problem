import pytest


def week_days(month, day, year):
    """
    function for get the week_days
    :param month: for accessing month
    :param day: for accessing day
    :param year: for accessing year
    :return: return corresponding week days
    """
    y = year - (14 - month) // 12
    x = y + y//4 - y//100 + y//400
    m = month + 12*((14-month)//12)-2
    d = (day + x + 31*m//12) % 7

    return d


def test_week_days():
    assert week_days(5, 10, 2022) == 2


if __name__ == "__main__":
    output = week_days(5, 10, 2022)

    if output == 0:
        print("SUNDAY")
    elif output == 1:
        print("MONDAY")
    elif output == 2:
        print("TUESDAY")
    elif output == 3:
        print("WEDNESDAY")
    elif output == 4:
        print("THURSDAY")
    elif output == 5:
        print("FRIDAY")
    elif output == 6:
        print("SATURDAY")

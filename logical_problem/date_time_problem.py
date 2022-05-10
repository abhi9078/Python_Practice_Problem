from datetime import date


def date_time():
    """
    function for get current date and time
    :return: date and time of today
    """
    today = date.today()
    return today


def date_time_in_string():
    """
    function for get date time as string
    :return: string value of date and time
    """
    dt = date.today()
    str_value = date.isoformat(dt)  # to convert date time to string
    return str_value


if __name__ == "__main__":
    result = date_time()
    print("today date is: ", result)
    print(type(result))
    result1 = date_time_in_string()
    print("today date in string: ", result1)
    print(type(result1))
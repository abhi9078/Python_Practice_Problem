
def wind_chill(t, v):
    """
    function will calculate wind chill
    :param t: get temperature value in fahrenheit
    :param v: get wind speed in mile per hour
    :return: calculated wind chill
    """
    if t <= 50 and (v >= 120 or v <= 3):
        wind = 35.74 + 0.6215*t + (0.4275*t - 35.75)*v**0.16
        print("wind chill is: ", wind)
    else:
        print("Required Temperature value is less than 50 and wind speed is more than 120 or less than 3")


if __name__ == "__main__":
    temp = int(input("please enter temperature vlue in fahrenheit: "))
    wind_speed = int(input("please enter wind speed in miles per hour"))
    wind_chill(temp, wind_speed)
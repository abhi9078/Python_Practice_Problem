import pytest


def temperature_conversion(conv, option):
    """
    function for temperature conversion
    :param conv: choosing different conversion
    :param option: changing option
    :return: desire output
    """
    if conv == "c to f":
        return (option * 9/5)+32
    if conv == "f to c":
        return (option-32) * 5/9


def test_my_func():
    assert temperature_conversion("c to f", 32) == 89.6


if __name__ == "__main__":
    conversion = ""
    print("Please select the conversion: ")
    choose = int(input("1. Celsius to Fahrenheit: "
                       "\n2. Fahrenheit to Celsius"))
    if choose == 1:
        conversion = "c to f"
        temp = int(input("Please enter value in Celsius"))
        output = temperature_conversion(conversion, temp)
        print(f"Output is: {output} fahrenheit")
    elif choose == 2:
        conversion = "f to c"
        temp = int(input("Please enter value in Fahrenheit "))
        output = temperature_conversion(conversion, temp)
        print(f"Output is: {output} celsius")
    else:
        print("please select 1 or 2")




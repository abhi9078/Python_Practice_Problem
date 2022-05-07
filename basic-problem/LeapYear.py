year = int(input("please enter a year to check for leap year: "))

if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print("This year is a Leap year", year)

else:
    print("This year is not a Leap year", year)
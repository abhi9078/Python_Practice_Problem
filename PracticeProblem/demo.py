def leap_year(year):
    if year > 999 and year < 10000:
        if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
            print("Entered year {0} is leap year" .format(year))
        else:
            print("Entered year {0} is not a leap year" .format(year))
    else:
        print("Enter a four digit number")


if __name__ == "__main__":
    year = int(input("Enter a year"))
    leap_year(year)

def get_start_day(year, month):
    date = 1
    y = year - (14 - month) // 12
    x = y + y // 4 - y // 100 + y // 400
    m = month + 12 * ((14 - month) // 12) - 2
    d = (date + x + 31 * m // 12) % 7
    return d


def print_date(mm, yy):
    total_day = 0
    even_m = [1, 3, 5, 7, 8, 10, 12]
    odd_m = [4, 6, 9, 11]
    if mm in even_m:
        total_day = 31
        return total_day
    elif mm in odd_m:
        total_day = 30
        return total_day
    else:
        if (yy % 400 == 0) or (yy % 100 != 0 and yy % 4 == 0):
            total_day = 29
            return total_day

        else:
            total_day = 28
            return total_day


if __name__ == "__main__":
    week_days = ["S", "M", "T", "W", "Th", "F", "S"]
    week_lt = [" ", " ", " ", " ", " ", " ", " ",
               " ", " ", " ", " ", " ", " ", " ",
               " ", " ", " ", " ", " ", " ", " ",
               " ", " ", " ", " ", " ", " ", " ",
               " ", " ", " ", " ", " ", " ", " ",
               " ", " ", " ", " ", " ", " ", " "]

    year = int(input("Enter Year"))
    month = int(input("Enter Month"))

    td = print_date(month, year)

    day = get_start_day(year, month)
    if day == 0:
        start = 0
        for i in range(1, td+1):
            week_lt[start] = i
            start += 1
    if day == 1:
        start = 1
        for i in range(1, td+1):
            week_lt[start] = i
            start += 1
    if day == 2:
        start = 2
        for i in range(1, td+1):
            week_lt[start] = i
            start += 1
    if day == 3:
        start = 3
        for i in range(1, td+1):
            week_lt[start] = i
            start += 1
    if day == 4:
        start = 4
        for i in range(1, td+1):
            week_lt[start] = i
            start += 1
    if day == 5:
        start = 5
        for i in range(1, td+1):
            week_lt[start] = i
            start += 1
    if day == 6:
        start = 6
        for i in range(1, td+1):
            week_lt[start] = i
            start += 1

    print(f"{week_days[0]}   {week_days[1]}   {week_days[2]}   {week_days[3]}   {week_days[4]}   "
          f"{week_days[5]}   {week_days[6]}")

    print(f"{week_lt[0]}   {week_lt[1]}   {week_lt[2]}   {week_lt[3]}   {week_lt[4]}   {week_lt[5]}   {week_lt[6]}\n"
          f"{week_lt[7]}   {week_lt[8]}   {week_lt[9]}   {week_lt[10]}  {week_lt[11]}  {week_lt[12]}  {week_lt[13]}\n"
          f"{week_lt[14]}  {week_lt[15]}  {week_lt[16]}  {week_lt[17]}  {week_lt[18]}  {week_lt[19]}  {week_lt[20]}\n"
          f"{week_lt[21]}  {week_lt[22]}  {week_lt[23]}  {week_lt[24]}  {week_lt[25]}  {week_lt[26]}  {week_lt[27]}\n"
          f"{week_lt[28]}  {week_lt[29]}  {week_lt[30]}  {week_lt[31]}  {week_lt[32]}  {week_lt[33]}  {week_lt[34]}\n"
          f"{week_lt[35]}  {week_lt[36]}  {week_lt[37]}  {week_lt[38]}  {week_lt[39]}  {week_lt[40]}  {week_lt[41]}\n")




def sum_of_number(list_input):
    list_sum = []

    for i in range(0, len(list_input)-1):
        result = list_input[i] + list_input[i + 1]
        list_sum.append(result)

    return list_sum


if __name__ == "__main__":
    lt = [2, 4, 6, 7, 9]
    print(sum_of_number(lt))

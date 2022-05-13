
def my_func(input_string):
    """
    function for count vowels and consonant in a string
    :param input_string: given string
    :return: count value
    """
    count_vowels = 0
    count_consonants = 0

    for i in input_string:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            count_vowels = count_vowels + 1
        elif i != ' ':
            count_consonants = count_consonants + 1

    return count_vowels, count_consonants


if __name__ == "__main__":
    string_input = input("Enter a string")
    in_str = string_input.lower()
    output = my_func(in_str)
    print("Number of vowels and consonant", output)


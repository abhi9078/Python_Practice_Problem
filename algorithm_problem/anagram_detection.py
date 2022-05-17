def reverse(str_in):
    return str_in[::-1]


def anagram_detection(str1, str2):
    """
    function for checking anagram
    :param str1: first string
    :param str2: second string
    :return: anagram detection
    """
    first_string = reverse(str1)

    if first_string == str2:
        return "Anagram Detected"
    else:
        return "Not an anagram"


if __name__ == "__main__":
    string1 = "racecar"
    string2 = "racecar"

    output = anagram_detection(string1, string2)
    print(output)

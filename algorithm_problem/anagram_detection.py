def anagram_detection(str1, str2):
    """
    function for checking anagram
    :param str1: first string
    :param str2: second string
    :return: anagram detection
    """
    first_string = sorted(str1)
    second_string = sorted(str2)

    if first_string == second_string:
        return "Anagram Detected"
    else:
        return "Not an anagram"


if __name__ == "__main__":
    string1 = "listen"
    string2 = "silent"

    output = anagram_detection(string1, string2)
    print(output)

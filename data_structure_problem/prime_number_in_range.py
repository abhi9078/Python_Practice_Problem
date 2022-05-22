def primes(n):
    """
    function for checking prime number in a given range
    :param n: last range of number
    :return: prime numbers
    """
    array = [i for i in range(2, n + 1)]
    p = 2
    pr = []

    while p <= n:
        i = 2 * p
        while i <= n:
            array[i - 2] = 0
            i += p
        p += 1

    for num in array:
        if num > 0:
            pr.append(num)

    return pr


if __name__ == "__main__":
    p_range = 1000
    output = primes(p_range)
    print("Prime number in range 0-100 are: ", output[:25])
    print("Prime number in range 100-200 are: ", output[25:46])
    print("Prime number in range 200-300 are: ", output[46:62])
    print("Prime number in range 300-400 are: ", output[62:78])
    print("Prime number in range 400-500 are: ", output[78:95])
    print("Prime number in range 500-600 are: ", output[95:109])
    print("Prime number in range 600-700 are: ", output[109:125])
    print("Prime number in range 700-800 are: ", output[125:139])
    print("Prime number in range 800-900 are: ", output[139:154])
    print("Prime number in range 900-1000 are: ", output[154:])

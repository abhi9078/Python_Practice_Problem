def primes(n):
    """
    function for getting prime number in range
    :param n: last range of input
    :return:
    """
    array = [i for i in range(2, n+1)]
    p = 2

    while p <= n:
        i = 2*p
        while i <= n:
            array[i-2] = 0
            i += p
        p += 1

    return [num for num in array if num > 0]


def anagram(a):
    """
    function for getting anagram number in prime number
    :param a:getting a list of prime number
    :return:anagram numbers
    """
    # initialize a list
    anagram_list = []
    for i in a:
        for j in a:
            if i != j and (sorted(str(i)) == sorted(str(j))):
                anagram_list.append(i)
    return anagram_list


if __name__ == '__main__':
    p_range = 1000
    p_out = primes(p_range)
    print("Prime Number with in 1000 are ", p_out)
    a_out = anagram(p_out)
    print("Anagram Number in that Prime numbers are: ", a_out)

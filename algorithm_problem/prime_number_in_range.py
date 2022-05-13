def prime_number():
    """
    function for collecting prime number with in 1000
    :return: prime numbers 
    """
    for i in range(2, 1000):
        count = 0
        j = 1
        temp = i
        while temp != 0:
            if i % j == 0:
                count = count + 1
            j = j+1
            temp -= 1

        if count == 2:
            yield i


if __name__ == "__main__":
    output = prime_number()
    print("Prime number with in 1000 are: ")
    for num in output:
        print(num)

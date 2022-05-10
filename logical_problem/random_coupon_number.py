import random


def generate(amount):
    """
    function for generating random number
    :param amount: last range output
    :return: return different random coupon number
    """
    for x in range(0, amount):
        a = random.randint(1000, 9999)
        a = str(a)
        b = random.randint(1000, 9999)
        b = str(b)
        c = random.randint(1000, 9999)
        c = str(c)

        total = ""
        total = a + "" + b + "" + c
        print(total)


if __name__ == "__main__":
    output = int(input("How many coupons do you want to generate: "))
    generate(output)
    print("\nCode's have been generated!")

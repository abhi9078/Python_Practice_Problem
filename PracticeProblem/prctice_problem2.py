class Calcualtor:
    def __init__(self, num1, num2):
        """
        constructor for initialising value
        :param num1: first number
        :param num2: second number
        :return: initialise the value
        """
        self.num1 = num1
        self.num2 = num2

    def add(self):
        """
        function for addition operation
        :return: addition of two number
        """
        return self.num1 + self.num2

    def sub(self):
        """
        function for subtraction
        :return:subtraction of two number
        """
        return self.num1 - self.num2

    def mul(self):
        """
        function for multiplication
        :return: multiplication of two numbr
        """
        return self.num1 * self.num2

    def div(self):
        """
        function for division
        :return: division of two number
        """
        return self.num1 / self.num2

    def operation(self, ope):
        """
        function for different mathematical operation
        :param ope: accept one operator as string
        :return: desire operation
        """
        if ope == "+":
            return self.num1 + self.num2
        elif ope == "-":
            return self.num1 - self.num2
        elif ope == "*":
            return self.num1 * self.num2
        elif ope == "/":
            return self.num1 / self.num2


if __name__ == "__main__":
    obj = Calcualtor(10, 20)
    # print(obj.add())
    # print(obj.sub())
    # print(obj.mul())
    # print(obj.div())
    #
    # print(obj.operation("+"))
    # print(obj.operation("-"))
    # print(obj.operation("*"))
    print(obj.operation("/"))



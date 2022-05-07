

def my_function(num1, num2, ope):
    if ope == "+":
        return num1+num2
    elif ope == "-":
        return num1 - num2
    elif ope == "*":
        return num1 * num2
    elif ope == "/":
        return num1 / num2


if __name__ == "__main__":
    num1 = 20
    num2 = 10
    addition = my_function(num1, num2, "+")
    sub = my_function(num1, num2, "-")
    mul = my_function(num1, num2, "*")
    div = my_function(num1, num2, "/")
    print("Addition is: ", addition)
    print("Substraction is: ", sub)
    print("Multiplication is: ", mul)
    print("Division is: ", div)
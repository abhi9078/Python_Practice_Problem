num = int(input("Please enter a number"))
fact = 1
while num > 0:
    fact = fact * num
    num = num - 1

print("The factorial is: ", fact)
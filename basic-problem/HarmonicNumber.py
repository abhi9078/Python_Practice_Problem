num = int(input("Enter the range"))
result = 0
start = 1
while start <= num:
    result = result + 1/start
    start = start+1

print("The harmonic number series is: ", result)

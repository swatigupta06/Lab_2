#question3
x = int(input("Enter the number:"))
y = int(input("Enter second number:"))
if x < 0 or y < 0:
    print("invalid input")
elif y % x == 0:
    print("y is divisble by x")
else:
    print("y is not divisble by x") 
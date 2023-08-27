#question5
r = int(input("Enter the radius of circle:"))
Area = 3.14 * r * r
if r < 1 or r > 100:
    print("values are not accepted")
else:
    print(Area)
#question8
year = int(input("enter the year: "))

if year%400==0 and year%100==0:
    print("year is leap")
elif year%4==0 and year%100!=0:
    print("year is leap")
else:
    print("year is not leap")
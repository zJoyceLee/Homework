year=int(input("Please input year(>999): "))
if (year%400==0) or (year%4==0 and year%100!=0):
    print("Year: %d, is a leap year."%year)
else:
    print("Year: %d, is not a leap year."%year)

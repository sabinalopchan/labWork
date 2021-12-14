# Check whether the given year is leap year or not. If year is leap print ‘LEAP YEAR’ else
# print ‘COMMON YEAR’.
# Hint: • a year is a leap year if its number is exactly divisible by 4 and is not
# exactly divisible by 100
# • a year is always a leap year if its number is exactly divisible by 40

year=int(input("enter year:"))
if (year%4)==0 and (year%100)!=0 or (year%400)==0:
    print("leap year")
else:
    print("common year")

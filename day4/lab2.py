# Write a Python program to sum three given integers. However,
#  if two or more values are equal sum will be zero.

a=10
b=20
c=30
sum=a+b+c
if a==b==c or a==b or a==c or b==c:
    print("sum is 0")
else:
    print("sum of three integers is",sum)    
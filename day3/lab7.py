# Given a positive real number, print its fractional part. 


a=float(input("enter the number:"))
x,y=math.modf(a)
print(x)
print(y)
# Given three integers, print the smallest one. (Three integers should be user input) 

num1=int(input("enter first integer:"))
num2=int(input("enter second integer:"))
num3=int(input("enter third integer:"))
if num1<num2 and num1<num3:
    print("smallest integer is",num1)
elif num2<num1 and num2<num3:
    print("smallest integer is",num2)
else:
    print("smallest integer is",num3)    



# sum of first ten even  number
sum=0
for num in range(1,11):
    if(num%2==0):
        sum+=num
print (f"Sum of first ten even number is {sum}")

# sum of first ten odd number
sum=0
for num in range(1,10):
    if(num%2!=0):
        sum+=num
print (f"Sum of first ten odd number is {sum}")
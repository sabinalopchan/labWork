# WAP which accepts marks of four subjects and display total marks, 
# percentage and grade. Hint: more than 70% –> distinction, more than 60% –> first, 
# more than 40% –> pass, less than 40% –> fail 

programming=int(input("Enter marks of programming:"))
software=int(input("Enter marks of software:"))
network=int(input("Enter marks of network:"))
database=int(input("Enter marks of database:"))
total=programming + software + network + database
print(total)
print("total marks is", total)
percentage=(total / 400) * 100
print("total percentage is", percentage, "%)")
if percentage>70:
    print("distinction")
elif percentage>60:
    print("first division")
elif percentage>40:
    print("pass")
else:
    print("fail")          


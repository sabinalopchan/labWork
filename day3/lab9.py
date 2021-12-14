username=input("Enter username:")
password=input("Enter password:")
for i in range(0,3):
    print("Enter your credentials")
    username1=input("enter your username:")
    password1=input("enter your password:")
    if username==username1 and password==password1:
        print("you are successfully logged in")
        break
    else:
        if (username!=username1 or password!=password1):
            print("invalid credentials")
else:
    print("3 attempt finished")
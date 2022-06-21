a=int(input("Enter Number  "))
if(a%2==0):
    print("even")
else:
    print("odd")

x=int(input("Enter Number "))
if(x>0) and (x<25):
    print("Valid Number")
    if(x<=12):
        print("Good Morning")
    elif(x>12):
        print("Good Evnining")
else:
    print("Invalid Number ")

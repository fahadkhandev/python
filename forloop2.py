# Tables 
a=int(input("Enter Table : " ))
print("Table of ",a)
for index in range(1,11):
    print(a,"*",index,"=",a*index)

# Tuples
tuple=("Fahad"+"Khan",3,0,2)
for elements in tuple:
    print(elements,end="")

# List
list=["khan",4,2,0]*5
for elements in list:
    print(elements,end="")
list=[43,23,45,3,234,5463,123,33,4,2221]
for elements in range(len(list)):
    print(list[elements])

# Print value in list With RunTime 
list=[]
n=int(input("Enter Limit : "))
print("Enter Elements ")
for index in range(0,n):
    a=int(input())
    list.append(a)
print("Elements in list = ",list)
# Odd Numbers 
print("Odd Numbers in list are : ")
for e in list:
    if(e%2!=0):
        print(e,end=" ")
print()
# Even Numbers
print("Even NUmber in list are :")
for e in list:
    if(e%2==0):
        print(e,end=" ")
# Hardcoding 
l=8
w=4
for len in range(8):
    for wid in range(4):
        print("*",end="")
    print()
#RunTime Value
l=int(input("enter length : "))
w=int(input("Enter Width : "))
s=input("Enter Symbol : ")
for len in range(l):
    for width in range(w):
        print(s,end="")
    print()
area=l*w
print("Area = ",area)

# Factorial 
n=int(input("Enter Number : "))
fact=1
for index in range(1,n+1):
    fact=fact*index
print("Factorial of ",n,"=",fact)